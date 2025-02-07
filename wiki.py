import wikipediaapi
import json
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, Trainer, TrainingArguments
import torch
from torch.utils.data import Dataset, DataLoader
import pandas as pd
from sklearn.model_selection import train_test_split

# Define User-Agent (Replace with your own info)
USER_AGENT = "YourName/1.0 (your_email@example.com)"

# Initialize Wikipedia API
wiki = wikipediaapi.Wikipedia(language="en", user_agent=USER_AGENT)

# List of Wikipedia pages to extract
pages = [
    "Strand Campus", 
    "King's Building, London", 
    "Screen Studies Group, London", 
    "Liddell Hart Centre for Military Archives",
    "Roman Baths, Strand Lane",
    "Hyde Park, London",
    "Regent's Park", 
    "Tower of London"
]

# Extract Wikipedia content
dataset = []
for topic in pages:
    page = wiki.page(topic)
    if page.exists():
        if (page.title != "Roman Baths, Strand Lane") and (page.title != "Roman Baths, Strand Lane") and (page.title != "Regent's Park") and (page.title != "Tower of London"):
            dataset.append({"title": page.title, "content": page.text, "category": "outdoor"})
        else:
            dataset.append({"title": page.title, "content": page.text, "category": "indoor"})
        print(f"✅ Extracted: {page.title}")
    else:
        print(f"❌ Page not found: {topic}")

# Save dataset to JSON
with open("wikipedia_multi.json", "w", encoding="utf-8") as f:
    json.dump(dataset, f, indent=4, ensure_ascii=False)

print("✅ Wikipedia dataset saved as 'wikipedia_multi.json'.")


print("Saved multiple pages to wikipedia_multi.json")

# Load pre-trained DistilBERT model and tokenizer
model_name = 'distilbert-base-uncased'  # Use the base model
tokenizer = DistilBertTokenizer.from_pretrained(model_name)
model = DistilBertForSequenceClassification.from_pretrained(model_name, num_labels=2)  # 2 labels: "indoor", "outdoor"
# Load the dataset from the JSON file
with open("wikipedia_multi.json", "r") as file:
    data = json.load(file)

# Check the data
print(data[:2])  # Display the first two rows of the data
# Initialize the DistilBERT tokenizer
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')

# Extract text and labels from the loaded dataset
# Combine title and content into a single text string for each entry
texts = [entry["title"] + " " + entry["content"] for entry in data]

# Label mapping (outdoor = 0, indoor = 1)
label_map = {"outdoor": 0, "indoor": 1}

# Convert the string labels into numeric values
labels = [label_map[entry["category"]] for entry in dataset]

# Tokenize the texts
encodings = tokenizer(texts, padding=True, truncation=True, max_length=512, return_tensors="pt")

# Convert labels to tensor
labels_tensor = torch.tensor(labels)
class ActivityDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

# Create dataset
train_dataset = ActivityDataset(encodings, labels_tensor)
train_dataloader = DataLoader(train_dataset, batch_size=8, shuffle=True)
# Load the pre-trained DistilBERT model for sequence classification
model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=2)

# Split the dataset into training and validation sets (80% train, 20% eval)
train_texts, eval_texts, train_labels, eval_labels = train_test_split(texts, labels, test_size=0.2, random_state=42)

# Tokenize the texts for both train and eval sets
train_encodings = tokenizer(train_texts, padding=True, truncation=True, max_length=512, return_tensors="pt")
eval_encodings = tokenizer(eval_texts, padding=True, truncation=True, max_length=512, return_tensors="pt")

# Convert labels to tensor
train_labels_tensor = torch.tensor(train_labels)
eval_labels_tensor = torch.tensor(eval_labels)

# Create Dataset objects for training and evaluation
train_dataset = ActivityDataset(train_encodings, train_labels_tensor)
eval_dataset = ActivityDataset(eval_encodings, eval_labels_tensor) 

# Define training arguments
training_args = TrainingArguments(
    output_dir='./results',           # Directory to store model checkpoints
    evaluation_strategy='epoch',      # Evaluate at the end of every epoch
    per_device_train_batch_size=8,    # Batch size for training
    num_train_epochs=3,              # Number of training epochs
    logging_dir='./logs',             # Directory for logs
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,  # Pass the eval dataset here
)

# Start training the model
trainer.train()
# Define class labels
classes = ['indoor', 'outdoor']

""" # Function to predict activity class
def predict_activity(text):
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_id = torch.argmax(logits).item()
    return classes[predicted_class_id]

# Example of predicting a new activity
activity = "Buckingham Palace"
predicted_class = predict_activity(activity)
print(f"The activity '{activity}' is classified as: {predicted_class}")
 """

def predict_activity(text, wiki_page_name=None):
    """
    Predicts if the activity described in the input text is indoor or outdoor.
    Optionally, fetches and includes content from a Wikipedia page for more context.
    
    Parameters:
        text (str): The input activity description.
        wiki_page_name (str, optional): The name of the Wikipedia page to fetch additional context from.
        
    Returns:
        str: The predicted activity category ("indoor" or "outdoor").
    """
    
    # Fetch the Wikipedia page content (if provided)
    if wiki_page_name:
        page = wiki.page(wiki_page_name)
        if page.exists():
            wiki_content = page.text
        else:
            wiki_content = ""
            print(f"❌ Wikipedia page '{wiki_page_name}' not found.")
    else:
        wiki_content = ""
    
    # Combine the input text and the Wikipedia page content (if available)
    combined_text = text + " " + wiki_content
    
    # Tokenize the combined content
    inputs = tokenizer(combined_text, return_tensors='pt', padding=True, truncation=True, max_length=512)
    
    # Run the model to get the prediction
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Get the predicted class
    logits = outputs.logits
    predicted_class_id = torch.argmax(logits).item()
    
    return classes[predicted_class_id]

# Example usage:
activity = "London Eye"
wiki_page_name = "London Eye"  # Example Wikipedia page to fetch context from
predicted_class = predict_activity(activity, wiki_page_name)
print(f"The activity '{activity}' is classified as: {predicted_class}")

