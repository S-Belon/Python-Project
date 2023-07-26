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

