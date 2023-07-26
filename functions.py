"""
Module: solar_flare_module

This module provides a function to calculate the duration of solar flares from the 'FLR' DataFrame.

Functions:
- flr_duration(z): Calculate the duration of solar flares and add a new column 'duration' to the DataFrame.

"""
import pandas as pd

def flr_duration(z):
    """

    Calculate the duration of solar flares from the 'FLR' DataFrame.

    This function takes the 'FLR' DataFrame, assumed to be part of the 'data_frames' dictionary,
    and converts the 'beginTime' and 'endTime' columns to datetime format. Then, it calculates
    the duration of each solar flare and adds a new column 'duration' to the DataFrame.

    Parameters:
    None (The function assumes that 'FLR' DataFrame is available in the 'data_frames' dictionary.)

    Returns:
    None (The function modifies the 'FLR' DataFrame in-place, adding the 'duration' column.)

    Example:
    If 'FLR' DataFrame has columns ['beginTime', 'endTime'], the function will add a new column
    'duration' containing the duration of each solar flare in minutes.

    """
    # Convert the start time and end time columns to datetime format
    z['beginTime'] = pd.to_datetime(z['beginTime'])
    z['endTime'] = pd.to_datetime(z['endTime'])

    # Calculate the duration of solar flares and add a new column
    z['duration'] = (z['endTime'] - z['beginTime']).dt.total_seconds() / 60

