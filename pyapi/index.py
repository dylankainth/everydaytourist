from fastapi import FastAPI
import requests
from fastapi import Request

app = FastAPI()

@app.get("/pyapi")
def hello_world():

    return {"message": "Hello World", "api": "all online"}

@app.post("/pyapi/generateRanking")
async def generate_ranking(request: Request):
    body = await request.json()

    print(body)
    # Fixed the rounding issue and corrected variable names
    lat = body['location']['coords']['latitude']
    lon = body['location']['coords']['longitude']

    radius = body['walkingDistance']

    url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&list=geosearch&gsradius={radius}&gscoord={lat}|{lon}"

    # Make API request
    response = requests.get(url)

    return {"message": "Request body printed", "body": response.json()}
