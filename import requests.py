import requests
import wikipedia
from datetime import datetime, timedelta

def extract_location_data(response):
    """Extracts title, lat, lon, and other details from Wikipedia API geosearch response."""
    data = response.json()  # Convert response to dictionary
    geosearch_list = data.get("query", {}).get("geosearch", [])  # Get the list of locations

    extracted_data = [
        {
            "pageid": location["pageid"],
            "title": location["title"],
            "lat": location["lat"],
            "lon": location["lon"],
            "dist": location["dist"],
        }
        for location in geosearch_list
    ]

    return extracted_data

def get_wikipedia_pageviews(article, days=90):
    end_date = datetime.today().strftime("%Y%m%d")  # Today's date
    start_date = (datetime.today() - timedelta(days=days)).strftime("%Y%m%d")  # 'days' ago

    # Wikipedia API Base URL
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
        "User-Agent": "MyWikiBot/1.0 (myemail@example.com)"
    }

    # Make the request
    response = requests.get(url, headers=headers)

    # Check response status
    if response.status_code == 200:
        data = response.json()

        # Calculate total views
        total_views = sum(item["views"] for item in data["items"])
        return total_views
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None


# Fixed the rounding issue and corrected variable names
lat = round(51.5114, 4)
lon = round(0.1190, 4)

radius = int(input("Radius? "))

url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&list=geosearch&gsradius={radius}&gscoord={lat}|{lon}"

# Make API request
response = requests.get(url)

# Extract data
locations = extract_location_data(response)

for location in locations:
    title = location["title"]
    views = get_wikipedia_pageviews(title)
    if views is not None:
        try:
            # Fetch and print summary
            summary = wikipedia.summary(title, sentences=2)
            print(summary)
        except wikipedia.exceptions.PageError:
            print(f"The page '{title}' does not exist on Wikipedia. Please check the spelling or try a different title.")
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"The page '{title}' is a disambiguation page. Possible options: {e.options}")
        except Exception as e:
            print(f"An error occurred: {e}")
        print("Total views for " + title +  "in the last 90 days: " + str(views))
