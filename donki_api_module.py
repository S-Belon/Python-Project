import requests
import pandas as pd

def download_donki_data():
    # Download all data from the DONKI API endpoint

    # Define the list of API endpoints
    api_endpoints = ['CME', 'CMEAnalysis', 'GST', 'IPS', 'FLR', 'SEP', 'MPC', 'RBE', 'HSS']

    # Define the common API parameters
    params = {
        'startDate': '2022-01-01',
        'endDate': '2022-12-31',
        'api_key': 'BkLnefy3MaYDPAsNO1vUZxXTepcIjKWPdZzfW2UY'  # Replace with your NASA API key
    }

    # Create an empty dictionary to store the DataFrame objects
    data_frames = {}

    # Iterate over the API endpoints and import data into DataFrame objects
    for endpoint in api_endpoints:
        # Define the API URL
        url = f'https://api.nasa.gov/DONKI/{endpoint}'
        
        # Send GET request to the API
        response = requests.get(url, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response as JSON
            data = response.json()
            
            # Convert the data into a DataFrame
            df = pd.DataFrame(data)
            
            # Store the DataFrame in the dictionary
            data_frames[endpoint] = df
        else:
            print(f'Error for endpoint {endpoint}:', response.status_code)

    # Return the dictionary of DataFrame objects
    return data_frames
