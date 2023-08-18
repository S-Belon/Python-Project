"""
Fetch Space Weather Data from NASA DONKI API

This script fetches data from various endpoints of the NASA DONKI (Space Weather Database of 
Notifications, Knowledge, Information) API for the last 365 days and converts the JSON response 
to pandas DataFrames. The data for specified API endpoints is stored in a dictionary.

Usage:
    Call the functions in this script to fetch and store data from the DONKI API.

API Endpoints:
    The functions in this script retrieve data for the following API endpoints:
    - 'CME': Coronal Mass Ejections
    - 'CMEAnalysis': CME Analysis
    - 'GST': Geomagnetic Storms
    - 'IPS': Interplanetary Shocks
    - 'FLR': Solar Flares
    - 'SEP': Solar Energetic Particles
    - 'MPC': Magnetopause Crossing
    - 'RBE': Radiation Belt Enhancement
    - 'HSS': High-Speed Streams

API Parameters:
    The functions use the following common API parameters:
    - 'startDate': The start date in the format 'YYYY-MM-DD' (365 days ago from the current date).
    - 'endDate': The end date in the format 'YYYY-MM-DD' (current date).
    - 'api_key'

Author:
    Your Name

"""
from datetime import datetime, timedelta
import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

def download_donki_data():
    """
    Download data from the NASA DONKI API for multiple endpoints and time range.

    This function fetches data from various endpoints of the NASA DONKI (Space Weather Database of 
    Notifications, Knowledge, Information) API for the last 365 days and converts the JSON response 
    to pandas DataFrames. The data for specified API endpoints is stored in a dictionary.

    Returns:
        dict: A dictionary containing DataFrame objects, where the keys are the API endpoint names,
              and the values are the corresponding DataFrames.

    Usage:
        Call this function to fetch and store data from the DONKI API.

    API Endpoints:
        The function retrieves data for the following API endpoints:
        - 'CME': Coronal Mass Ejections
        - 'CMEAnalysis': CME Analysis
        - 'GST': Geomagnetic Storms
        - 'IPS': Interplanetary Shocks
        - 'FLR': Solar Flares
        - 'SEP': Solar Energetic Particles
        - 'MPC': Magnetopause Crossing
        - 'RBE': Radiation Belt Enhancement
        - 'HSS': High-Speed Streams

    API Parameters:
        The function uses the following common API parameters:
        - 'startDate': The start date in the format 'YYYY-MM-DD' (365 days ago from the current date).
        - 'endDate': The end date in the format 'YYYY-MM-DD' (current date).
        - 'api_key'

    Example:
        # Call the function to download the data and store it in a dictionary of DataFrames
        data_frames = download_donki_data()
    """
    # Define the list of API endpoints
    api_endpoints = ['CME', 'CMEAnalysis', 'GST', 'IPS', 'FLR', 'SEP', 'MPC', 'RBE', 'HSS']

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
    Fetch data from the NASA DONKI API for multiple endpoints in the last 7 days.

    This function fetches data from various endpoints of the NASA DONKI (Space Weather Database of 
    Notifications, Knowledge, Information) API for the last 7 days and converts the JSON response 
    to pandas DataFrames. The data for specified API endpoints is stored in a dictionary.

    Returns:
        dict: A dictionary containing DataFrame objects, where the keys are the API endpoint names,
              and the values are the corresponding DataFrames containing data from the last 7 days.

    Usage:
        Call this function to fetch and store data from the DONKI API for the last 7 days.

    API Endpoints:
        The function retrieves data for the following API endpoints:
        - 'CME': Coronal Mass Ejections
        - 'CMEAnalysis': CME Analysis
        - 'GST': Geomagnetic Storms
        - 'IPS': Interplanetary Shocks
        - 'FLR': Solar Flares
        - 'SEP': Solar Energetic Particles
        - 'MPC': Magnetopause Crossing
        - 'RBE': Radiation Belt Enhancement
        - 'HSS': High-Speed Streams

    API Parameters:
        The function uses the following common API parameters:
        - 'startDate': The start date in the format 'YYYY-MM-DD' (7 days ago from the current date).
        - 'endDate': The end date in the format 'YYYY-MM-DD' (current date).
        - 'api_key'

    Returns:
        dict: A dictionary containing DataFrame objects, where the keys are the API endpoint names,
              and the values are the corresponding DataFrames containing data from the last 7 days.

    Example:
        # Call the function to fetch the last 7 days data and store it in a dictionary of DataFrames
        data_frames_last_7_days = fetch_last_7_days_data()
    """
    # Define the list of API endpoints
    api_endpoints = ['CME', 'CMEAnalysis', 'GST', 'IPS', 'FLR', 'SEP', 'MPC', 'RBE', 'HSS']

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