"""
donki_api_module.py - Python module to download data from the NASA DONKI API.

This module provides functions to download data from various endpoints of the NASA DONKI (Space Weather Database of 
Notifications, Knowledge, Information) API. It retrieves data for specified API endpoints and time range, converts 
the JSON response to pandas DataFrames, and stores them in a dictionary.

Functions:
- download_donki_data: Downloads data from multiple API endpoints and returns a dictionary of DataFrame objects.

Usage:
1. Place this module (donki_api_module.py) in the same directory as your main script.
2. Import the module and call the download_donki_data function to fetch the data.
"""

import requests
import pandas as pd


def download_donki_data():
    api_endpoints = [
        "CME",
        "CMEAnalysis",
        "GST",
        "IPS",
        "FLR",
        "SEP",
        "MPC",
        "RBE",
        "HSS",
    ]
    params = {
        "startDate": "2022-01-01",
        "endDate": "2022-12-31",
        "api_key": "BkLnefy3MaYDPAsNO1vUZxXTepcIjKWPdZzfW2UY",
    }
    data_frames = {}
    timeout = 100
    for endpoint in api_endpoints:
        url = f"https://api.nasa.gov/DONKI/{endpoint}"

        try:
            response = requests.get(url, params=params, timeout=timeout)
            if response.status_code == 200:
                data = response.json()

                df = pd.DataFrame(data)

                data_frames[endpoint] = df
            else:
                print(f"Error for endpoint {endpoint}:", response.status_code)
        except requests.exceptions.Timeout:
            print(f"Timeout occurred for endpoint {endpoint}")
    return data_frames
