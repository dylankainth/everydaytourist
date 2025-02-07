from transformers import pipeline
import wikipediaapi
import json

# Initialize Zero-Shot Classification Pipeline
zero_shot_classifier = pipeline("zero-shot-classification")

# Define candidate labelsS
candidate_labels = ["indoor", "outdoor"]

# Initialize Wikipedia API
USER_AGENT = "your-user-agent"  # Replace with your custom user-agent
wiki = wikipediaapi.Wikipedia(language="en", user_agent=USER_AGENT)

# List of Wikipedia pages to extract
pages = [
    "Strand Campus", 
    "King's Building, London", 
    "Screen Studies Group, London", 
    "Liddell Hart Centre for Military Archives",
    "King George III Museum",
    "The Dickson Poon School of Law",
    "Roman Baths, Strand Lane",
    "St Mary le Strand (parish)"
]

# Extract Wikipedia content and classify as indoor or outdoor
dataset = []
for topic in pages:
    page = wiki.page(topic)
    if page.exists():
        # Classify content as indoor or outdoor
        result = zero_shot_classifier(page.text, candidate_labels)
        predicted_label = result['labels'][0]  # The label with the highest score
        
        # Append the result to the dataset
        dataset.append({
            "title": page.title,
            "content": page.text,
            "category": predicted_label  # 'indoor' or 'outdoor'
        })
        print(f"✅ Extracted and classified: {page.title} as {predicted_label}")
    else:
        print(f"❌ Page not found: {topic}")

# Save dataset to JSON
with open("wikipedia_with_activity_classification.json", "w", encoding="utf-8") as f:
    json.dump(dataset, f, indent=4, ensure_ascii=False)

print("✅ Wikipedia dataset saved as 'wikipedia_with_activity_classification.json'.")
