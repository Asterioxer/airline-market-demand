from flask import Flask, render_template, request
import requests
import pandas as pd
import os
from dotenv import load_dotenv
import cohere

# Load API keys
load_dotenv()
AVIATIONSTACK_API_KEY = os.getenv("AVIATIONSTACK_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

app = Flask(__name__)

# Function to fetch flight data from AviationStack
def fetch_flight_data():
    url = f"http://api.aviationstack.com/v1/flights?access_key={AVIATIONSTACK_API_KEY}&limit=100"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("data", [])
    except Exception as e:
        print(f"API fetch error: {e}")
        return []

# Function to process and structure the data
def process_data(data):
    routes = []
    departures = []
    arrivals = []
    airlines = []

    for flight in data:
        dep = flight.get('departure', {}).get('iata', '')
        arr = flight.get('arrival', {}).get('iata', '')
        airline_name = flight.get('airline', {}).get('name', '')

        if dep and arr:
            route = f"{dep} → {arr}"
            routes.append(route)
            departures.append(dep)
            arrivals.append(arr)
            airlines.append(airline_name)

    df = pd.DataFrame({
        'route': routes,
        'dep': departures,
        'arr': arrivals,
        'airline': airlines
    })

    top_routes = df['route'].value_counts().head(10).to_dict()
    return df, top_routes

# Function to generate AI insight using Cohere
def generate_insight_from_data(route_counts):
    if not route_counts:
        return "No route data available to generate insights."

    summary_prompt = "Analyze the following flight route demand data and summarize key insights:\n"
    for route, count in route_counts.items():
        summary_prompt += f"- {route}: {count} flights\n"
    summary_prompt += "\nInsight:"

    try:
        co = cohere.Client(COHERE_API_KEY)
        response = co.generate(
            model="command-r-plus",
            prompt=summary_prompt,
            max_tokens=100,
            temperature=0.7
        )
        return response.generations[0].text.strip()
    except Exception as e:
        print(f"AI insight error: {e}")
        return "Insight generation failed due to API error."

# Flask route
@app.route('/', methods=['GET'])
def index():
    # Get filter parameters
    dep_filter = request.args.get('departure', '').upper()
    arr_filter = request.args.get('arrival', '').upper()
    airline_filter = request.args.get('airline', '')

    # Fetch and process data
    data = fetch_flight_data()
    full_df, top_routes = process_data(data)  # unfiltered data

    # Get full dropdown options BEFORE filtering
    unique_departures = sorted(full_df['dep'].dropna().unique())
    unique_arrivals = sorted(full_df['arr'].dropna().unique())
    unique_airlines = sorted(full_df['airline'].dropna().unique())

    # Create a filtered copy
    df = full_df.copy()
    if dep_filter:
        df = df[df['dep'] == dep_filter]
    if arr_filter:
        df = df[df['arr'] == arr_filter]
    if airline_filter:
        df = df[df['airline'] == airline_filter]

    # Update top routes after filtering
    filtered_route_counts = df['route'].value_counts().head(10).to_dict()

    # Generate AI-powered insight
    insight = generate_insight_from_data(filtered_route_counts)

    return render_template(
        "index.html",
        routes=filtered_route_counts,
        insight=insight,
        unique_departures=unique_departures,
        unique_arrivals=unique_arrivals,
        unique_airlines=unique_airlines,
        dep_filter=dep_filter,
        arr_filter=arr_filter,
        airline_filter=airline_filter
    )


if __name__ == "__main__":
    app.run(debug=True)
