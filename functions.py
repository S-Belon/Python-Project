import pandas as pd

def flr_duration(z):
    """
    Calculate the duration of solar flares.

    This function calculates the duration of solar flares based on the provided start time
    and end time columns in the DataFrame.

    Args:
        z (pandas.DataFrame): The input DataFrame containing solar flare data with start and end times.

    Returns:
        None. The function adds a 'duration' column to the DataFrame with the calculated durations in minutes.
    """
    # Convert the start time and end time columns to datetime format
    z['beginTime'] = pd.to_datetime(z['beginTime'])
    z['endTime'] = pd.to_datetime(z['endTime'])

    # Calculate the duration of solar flares and add a new column
    z['duration'] = (z['endTime'] - z['beginTime']).dt.total_seconds() / 60

def weekly_averages(x):
    """
    Calculate weekly averages of space weather data.

    This function calculates weekly averages of various space weather data including speed, half angle,
    latitude, longitude, and more. It groups the data by a weekly interval and aggregates the data points.

    Args:
        x (pandas.DataFrame): The input DataFrame containing space weather data with a time column.

    Returns:
        pandas.DataFrame: A DataFrame containing weekly averages of the specified space weather data.
    """
    # Assuming cme_df is your DataFrame and time21_5 column is already converted to datetime format
    x['time21_5'] = pd.to_datetime(x['time21_5'])

    # Group the data by the interval of 52 weeks and calculate the weekly averages
    x['time21_5_interval'] = x['time21_5'].dt.to_period('W').dt.start_time
    weekly_averages = x.groupby('time21_5_interval').agg({
    'time21_5': 'first',  # Use the first occurrence of time21_5 in the week
    'speed': 'mean',
    'halfAngle': 'mean',
    'latitude': 'mean',
    'longitude': 'mean',
    'type': lambda x: x.value_counts().index[0],  # Most frequent type in the week
    'isMostAccurate': 'any',  # Any value is True if at least one is True
    'associatedCMEID': lambda x: ', '.join(x),  # Combine IDs with comma if there are multiple
    'note': lambda x: x.iloc[0],  # Take the first note in the week
    'catalog': lambda x: x.iloc[0],  # Take the first catalog link in the week
    'link': lambda x: x.iloc[0]  # Take the first link in the week
    }).reset_index()

    # Drop the unnecessary column
    weekly_averages.drop(columns=['time21_5_interval'], inplace=True)
    
    return weekly_averages