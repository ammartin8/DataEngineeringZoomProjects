# Importing python libraries
from datetime import datetime as dt
from dotenv import load_dotenv
import dlt
from dlt.sources.helpers.rest_client import RESTClient
import os
import pandas as pd
import requests

load_dotenv()

API_BASE_URL = "https://api.coingecko.com/api/v3/"

key=os.getenv("API_KEY")

endpoint=f"coins/markets"

params={"vs_currency": "usd","precision": "2"}

headers = {"accept": "application/json", "x_cg_demo_api_key":key}

# Helper functions
def str_date_to_unix(string_date: str):
    date_object = dt.strptime(string_date, "%d-%m-%Y")
    unix_timestamp = int(date_object.timestamp())
    return unix_timestamp

def unix_to_str_date(unix_timestamp):
    date_object = dt.fromtimestamp(unix_timestamp)
    formatted_date = date_object.strftime("%d-%m-%Y")
    return formatted_date

def fetch_data():
    try:
        client = RESTClient(
            base_url=API_BASE_URL,
            headers=headers
        )
        response = client.get(endpoint, params=params)
        data = response.json()
    except:
        print("Issue fetching data")
    print("Data extracted")
    return data

print(fetch_data())
