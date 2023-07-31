import requests
import pandas as pd
from datetime import datetime, timedelta


def download_donki_data():
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
    # Define the list of API endpoints
    api_endpoints = ['CME', 'CMEAnalysis', 'GST', 'IPS', 'FLR', 'SEP', 'MPC', 'RBE', 'HSS']

    # Define the common API parameters
    api_key = 'BkLnefy3MaYDPAsNO1vUZxXTepcIjKWPdZzfW2UY'  # Replace with your NASA API key

    # Calculate the start and end dates for the last 365 days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)

    # Convert dates to the required format (YYYY-MM-DD)
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    # Create an empty dictionary to store the DataFrame objects
    data_frames = {}

    # Iterate over the API endpoints and import data into DataFrame objects
    for endpoint in api_endpoints:
        # Define the API URL with the updated start and end dates
        url = f'https://api.nasa.gov/DONKI/{endpoint}'
        params = {
            'startDate': start_date_str,
            'endDate': end_date_str,
            'api_key': api_key
        }
    
        # Send GET request to the API
        response = requests.get(url, params=params)
    
        # Check if the request was successful
        if response.status_code == 200:
            try:
                # Parse the response as JSON
                data = response.json()
            
                # Convert the data into a DataFrame
                df = pd.DataFrame(data)
            
                # Store the DataFrame in the dictionary
                data_frames[endpoint] = df
            except ValueError as e:
                print(f'Error parsing JSON for endpoint {endpoint}:', e)
        else:
            print(f'Error for endpoint {endpoint}:', response.status_code)
    return data_frames