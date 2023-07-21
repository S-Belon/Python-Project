import requests
import pandas as pd


def download_donki_data():
    """
    This function downloads data from multiple endpoints of the NASA DONKI
    (Space Weather Database of Notifications, Knowledge, Information) API.

    This function retrieves data from various API endpoints within the specified
    time range and converts the JSON response to pandas DataFrames.
    The fetched data is stored in a dictionary, where each key represents the API endpoint name, and
    each value is the corresponding DataFrame containing the API response data.

    Returns:
    dict: A dictionary containing DataFrames with the API response data for each endpoint.

    Raises:
    requests.exceptions.Timeout: If a request to the DONKI API times out.
    """
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
    timeout = 30
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
