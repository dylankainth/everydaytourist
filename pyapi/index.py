from fastapi import FastAPI
import requests
from fastapi import Request
import wikipedia
from datetime import datetime, timedelta
import os
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch
app = FastAPI()

# Load model and tokenizer from the saved folder
model_path = "DylanKainth/indooroutdoor"

model = DistilBertForSequenceClassification.from_pretrained(model_path)
tokenizer = DistilBertTokenizer.from_pretrained(model_path)

classes = ['indoor', 'outdoor']

# Prediction function
def predict_activity(text):
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_id = torch.argmax(logits).item()
    return classes[predicted_class_id]

@app.get("/pyapi")
def get_wikipedia_pageviews(article, days = 90):
    end_date = datetime.today().strftime("%Y-%m-%d")
    start_date = (datetime.today() - timedelta(days=days)).strftime("%Y-%m-%d")

    BASE_URL = "https;//wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{article}/daily/{start_date}/{end_date}"

    headers = {"User-Agent": "MyWikiBot/1.0 (myemail@example.com)"}

    response = requests.get(BASE_URL, headers=headers)

    if response.status_code == 200:
        data = response.json()
        total_views = sum([item['views'] for item in data['items']])
        return total_views
    else:
        print("Error: Unable to fetch data")

def hello_world():

    return {"message": "Hello World", "api": "all online"}


def get_wikipedia_nearby(radius, lat, lon):
    url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&list=geosearch&gsradius={radius}&gscoord={lat}|{lon}"

    # Make API request
    response = requests.get(url)

    responseData = response.json()

    return responseData['query']['geosearch']

def add_wikipedia_pageviews(mainData):

    end_date = datetime.today().strftime("%Y%m%d") 
    start_date = (datetime.today() - timedelta(days=90)).strftime("%Y%m%d")  

    for location in mainData:
     # Wikipedia API Base URL
        article = location['title']
        BASE_URL = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/{project}/{access}/{agent}/{article}/{granularity}/{start}/{end}"

        # Format API URL
        url = BASE_URL.format(
            project="en.wikipedia.org",
            access="all-access",
            agent="all-agents",
            article=article,
            granularity="daily",
            start=start_date,
            end=end_date
        )

         # Set User-Agent header (required)
        headers = {
            "User-Agent": "EveryDayTourist/1.0 (dylan.kainth@dylankainth.com)"
        }

        # Make the request
        response = requests.get(url, headers=headers)

        # Check response status
        if response.status_code == 200:
            data = response.json()

            # Calculate total views
            total_views = sum(item["views"] for item in data["items"])

            mainData[mainData.index(location)]['views'] = total_views

        else:
            print(f"Error {response.status_code}: {response.text}")
            return None

def add_walking_time(mainData, lat, lon):
    for location in mainData:
        # use osrm API to get walking time, url = https://osrm.services.dylankainth.com/
        url = f"https://osrm.services.dylankainth.com/route/v1/foot/{lon},{lat};{location['lon']},{location['lat']}?overview=false"

        # Make API request
        response = requests.get(url)

        responseData = response.json()

        #set they key of 'walkingTime' of location to the duration value from the response
        location['walkingTime'] = responseData['routes'][0]['duration']

def add_wikipedia_page_data(mainData):
    for location in mainData:
        # get the wikipedia page data
        page = wikipedia.page(location['title'])
        # get the summary of the page
        location['summary'] = page.summary

def add_prediction_data(mainData):
    for location in mainData:
        # predict the activity of the location
        location['activity'] = predict_activity(location['summary'])

@app.post("/pyapi/generateRanking")
async def generate_ranking(request: Request):
    body = await request.json()

    # Fixed the rounding issue and corrected variable names
    lat = body['location']['coords']['latitude']
    lon = body['location']['coords']['longitude']
    radius = body['walkingDistance']

    mainData = get_wikipedia_nearby(radius, lat, lon)
    add_wikipedia_pageviews(mainData)
    add_walking_time(mainData, lat, lon)
    add_wikipedia_page_data(mainData)
    add_prediction_data(mainData)

    # body['outdoorActivities'] is a boolean, filter the mainData based on the activity
    #if body['outdoorActivities']:
        #mainData = [location for location in mainData if location['activity'] == 'outdoor']
    #else:
        #mainData = [location for location in mainData if location['activity'] == 'indoor']

    return {"message": "all good", "body": mainData}

# get pageId from qsp and then go to wikipedia and get page info with that id
@app.get("/pyapi/getPage")
def get_page(id: int):
    page = wikipedia.page(pageid=id)
    return {"title": page.title, "summary": page.summary}