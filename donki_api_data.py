from datetime import datetime, timedelta
import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

def download_donki_data():
    """
    Download space weather data from NASA's DONKI API.

    This function downloads space weather data from the DONKI API for the last 365 days
    and returns the data in the form of DataFrame objects.

    Returns:
        dict: A dictionary containing DataFrame objects for different types of space weather data.
    """
    # Define the list of API endpoints
    api_endpoints = ['CME', 'CMEAnalysis', 'FLR']

    # Define the common API parameters
    api_key = os.getenv("api_key")

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


def data_7():
    """
    Download space weather data from NASA's DONKI API for the last 7 days.

    This function downloads space weather data from the DONKI API for the last 7 days
    and returns the data in the form of DataFrame objects.

    Returns:
        dict: A dictionary containing DataFrame objects for different types of space weather data.
    """
    # Define the list of API endpoints
    api_endpoints = ['CME', 'CMEAnalysis', 'FLR']

    # Define the common API parameters
    api_key = os.getenv("api_key")

    # Calculate the start and end dates for the last 365 days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)

    # Convert dates to the required format (YYYY-MM-DD)
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    # Create an empty dictionary to store the DataFrame objects
    df_7 = {}

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
                df_7[endpoint] = df
            except ValueError as e:
                print(f'Error parsing JSON for endpoint {endpoint}:', e)
        else:
            print(f'Error for endpoint {endpoint}:', response.status_code)
    return df_7