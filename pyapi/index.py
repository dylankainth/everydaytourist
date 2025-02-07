from fastapi import FastAPI
import requests
from fastapi import Request
import wikipedia
from datetime import datetime, timedelta

app = FastAPI()

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

        

@app.post("/pyapi/generateRanking")
async def generate_ranking(request: Request):
    body = await request.json()

    # Fixed the rounding issue and corrected variable names
    lat = body['location']['coords']['latitude']
    lon = body['location']['coords']['longitude']
    radius = body['walkingDistance']



    mainData = get_wikipedia_nearby(radius, lat, lon)
    add_wikipedia_pageviews(mainData)



    # for location in (responseData['query']['geosearch']):
    #     print(location['title'])
    #     title = location['title']
    #     views = get_wikipedia_pageviews(title)
    #     if views is not None

    


    # end_date = datetime.today().strfttime("%Y-%m-%d")
    # start_date = (datetime.today() - timedelta(days=90)).strftime("%Y-%m-%d")


    return {"message": "Request body printed", "body": mainData}
