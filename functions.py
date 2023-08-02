"""
Module: solar_flare_module

This module provides a function to calculate the duration of solar flares from the 'FLR' DataFrame.

Functions:
- flr_duration(z): Calculate the duration of solar flares and add a new column 'duration' to the DataFrame.

"""
import pandas as pd

def flr_duration(z):
    """
    Convert start time and end time columns to datetime format and calculate solar flare duration.

    This function takes a DataFrame 'z' containing solar flare information and assumes that the
    'beginTime' and 'endTime' columns are present in the DataFrame. It converts these columns to
    datetime format using pandas' pd.to_datetime() function. Then, it calculates the duration of
    each solar flare and adds a new column 'duration' to the DataFrame.

    Parameters:
    z (pandas.DataFrame): The DataFrame containing solar flare information.

    Returns:
    None: The function modifies the DataFrame 'z' in-place, adding the 'duration' column.

    Example:
    If 'z' DataFrame has columns ['beginTime', 'endTime'], the function will add a new column
    'duration' containing the duration of each solar flare in minutes.

    """
    
    # Convert the start time and end time columns to datetime format
    z['beginTime'] = pd.to_datetime(z['beginTime'])
    z['endTime'] = pd.to_datetime(z['endTime'])

    # Calculate the duration of solar flares and add a new column
    z['duration'] = (z['endTime'] - z['beginTime']).dt.total_seconds() / 60

def weekly_averages(x):
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