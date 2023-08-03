"""
This module provides functions for visualizing the space weather data.

Functions:
- flr_hist(x): Create a histogram of solar flare duration without outliers.

"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import calendar

def flr_hist(x):
    """
    Create a histogram of solar flare duration without outliers.

    This function takes a DataFrame 'x' containing information about solar flares,
    and it calculates the range of solar flare duration without outliers using
    quantiles (1st and 99th percentile). Then, it creates a histogram to visualize
    the distribution of solar flare durations without including the outliers.

    Parameters:
    x (pandas.DataFrame): A DataFrame containing solar flare information.

    Returns:
    None (The function displays the histogram plot).

    Example:
    flr_hist(data_frame)

    """
    # Calculate the range of solar flare duration without outliers
    lower_bound = x['duration'].quantile(0.01)
    upper_bound = x['duration'].quantile(0.99)

    # Create a histogram of the solar flare duration without outliers
    plt.hist(x['duration'], bins=20, range=(lower_bound, upper_bound))
    plt.xlabel('Solar Flare Duration (minutes)')
    plt.ylabel('Frequency')
    plt.title('Histogram of Solar Flare Duration (without outliers)')
    plt.show()

def flr_class(x):
    """
    Create a bar chart of solar flare class frequencies.

    This function takes a DataFrame 'x' containing information about solar flares,
    and it filters the DataFrame to include only rows with 'classType' values that
    occur more than 2 times. Then, it creates a bar chart to visualize the frequency
    distribution of solar flare classes with frequencies greater than 2.

    Parameters:
    x (pandas.DataFrame): A DataFrame containing solar flare information.

    Returns:
    None (The function displays the bar chart plot).

    Example:
    flr_class(data_frame)

    Notes:
    - The 'classType' column in the DataFrame 'x' must contain categorical values
      representing solar flare classes.
    - The bar chart displays the frequency distribution of solar flare classes
      that occur more than 2 times.
    - The x-axis represents the solar flare classes, and the y-axis represents
      the frequency count for each class.

    """
    # Filter the DataFrame to include only rows with 'classType' values that occur more than 2 times
    class_counts = x['classType'].value_counts()
    class_counts_filtered = class_counts[class_counts > 2]

    # Create a bar chart of the filtered classType
    class_counts_filtered.plot(kind='bar', rot=45)
    plt.xlabel('Solar Flare Class')
    plt.ylabel('Frequency')
    plt.title('Bar Chart of Solar Flare Class (Frequency > 2)')
    plt.show()

def hist_CME_speed(x):
    # Plot the CME speed distribution
    plt.hist(x['speed'], bins=20)
    plt.xlabel('CME Speed')
    plt.ylabel('Frequency')
    plt.title('Distribution of CME Speed')
    plt.show()

def flr_class_dist(x):
    # Assuming you have class_type_counts
    class_type_counts = x['classType'].value_counts().nlargest(10)

    # Plot the donut chart
    plt.figure(figsize=(8, 8))  # Set the size of the figure (optional)

    # Create the pie chart
    plt.pie(class_type_counts, labels=class_type_counts.index, autopct='%1.1f%%', startangle=90)

    # Draw a white circle at the center to create the donut effect
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    # Add a title to the donut chart
    plt.title("Distribution of classType (Donut Chart)")

    # Display the donut chart
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

def ts_halfangle(x):
    # Plot the time series for halfAngle, latitude, and longitude
    plt.figure(figsize=(12, 6))
    plt.plot(x['time21_5'], x['halfAngle'], marker='o', linestyle='-', color='g', label='Half Angle')
    plt.plot(x['time21_5'], x['latitude'], marker='o', linestyle='-', color='r', label='Latitude')
    plt.plot(x['time21_5'], x['longitude'], marker='o', linestyle='-', color='purple',    label='Longitude')

    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Time Series of Half Angle, Latitude, and Longitude')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Show the plot
    plt.show()

def ts_speed(x):
    # Plot the time series
    plt.figure(figsize=(12, 6))
    plt.plot(x['time21_5'], x['speed'], marker='o', linestyle='-', color='b')
    plt.xlabel('Date')
    plt.ylabel('Speed')
    plt.title('Time Series of Speed')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    # Show the plot
    plt.show()

def heat_map(x):
    # Assuming cme_df is your DataFrame and time21_5 column is already converted to datetime format
    x['time21_5'] = pd.to_datetime(x['time21_5'])

    # Bin the time21_5 column into 12 bins representing 12 weeks
    x['time21_5_bin'] = pd.cut(x['time21_5'], bins=12)

    # Map the day of the week to the corresponding integer value (0 - Monday, 1 - Tuesday, ..., 6 - Sunday)
    x['day_of_week'] = x['time21_5'].dt.dayofweek + 1  # Adjust day_of_week from 0-based to 1-based

    # Pivot the DataFrame to get the heatmap data
    heatmap_data = x.pivot_table(index='day_of_week', columns='time21_5_bin', values='speed', aggfunc='mean')

    # Convert Interval objects to strings for xticklabels
    heatmap_data.columns = heatmap_data.columns.astype(str)

    # Create the heatmap
    plt.figure(figsize=(12, 6))
    sns.heatmap(heatmap_data, cmap='YlGnBu')

    # Customize x-axis and y-axis tick labels
    plt.xticks(range(1, 13), range(1, 13))
    plt.yticks(range(1, 8), range(1, 8))

    # Add labels and title
    plt.xlabel('Time')
    plt.ylabel('Day of the Week')
    plt.title('Heatmap of Speed (Average) by Month and Day of the Week')

    # Show the plot
    plt.show()