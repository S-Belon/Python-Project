import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def flr_hist(x):
    """
    Create a histogram of solar flare duration without outliers.

    Args:
        x (pandas.DataFrame): The input DataFrame containing solar flare duration data.

    Returns:
        None. Displays the histogram.
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
    Create a bar chart of solar flare classes.

    Args:
        x (pandas.DataFrame): The input DataFrame containing solar flare class data.

    Returns:
        None. Displays the bar chart.
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
    """
    Create a histogram of CME speeds.

    Args:
        x (pandas.DataFrame): The input DataFrame containing CME speed data.

    Returns:
        None. Displays the histogram.
    """
    # Plot the CME speed distribution
    plt.hist(x['speed'], bins=20)
    plt.xlabel('CME Speed')
    plt.ylabel('Frequency')
    plt.title('Distribution of CME Speed')
    plt.show()

def flr_class_dist(x):
    """
    Create a donut chart of solar flare class distribution.

    Args:
        x (pandas.DataFrame): The input DataFrame containing solar flare class distribution data.

    Returns:
        matplotlib.figure.Figure: The Matplotlib figure containing the donut chart.
    """
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
    return plt 

def ts_halfangle(x):
    """
    Create a time series plot for Half Angle, Latitude, and Longitude.

    Args:
        x (pandas.DataFrame): The input DataFrame containing time series data.

    Returns:
        matplotlib.figure.Figure: The Matplotlib figure containing the time series plot.
    """
    # Create a Matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot the time series for halfAngle, latitude, and longitude
    ax.plot(x['time21_5'], x['halfAngle'], marker='o', linestyle='-', color='g', label='Half Angle')
    ax.plot(x['time21_5'], x['latitude'], marker='o', linestyle='-', color='r', label='Latitude')
    ax.plot(x['time21_5'], x['longitude'], marker='o', linestyle='-', color='purple', label='Longitude')

    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.set_title('Time Series of Half Angle, Latitude, and Longitude')
    
    # Set the tick labels on the x-axis with rotation
    x_ticks = pd.date_range(x['time21_5'].min(), x['time21_5'].max(), freq='MS')  # Create monthly tick positions
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_ticks.strftime('%Y-%m'), rotation=45)  # Format tick labels as 'YYYY-MM'
    
    ax.grid(True)
    ax.legend()
    plt.tight_layout()

    # Return the Matplotlib figure
    return fig

def ts_speed(x):
    """
    Create a time series plot for CME Speed.

    Args:
        x (pandas.DataFrame): The input DataFrame containing time series data.

    Returns:
        matplotlib.figure.Figure: The Matplotlib figure containing the time series plot.
    """
    # Create a Matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot the time series
    ax.plot(x['time21_5'], x['speed'], marker='o', linestyle='-', color='b')
    ax.set_xlabel('Date')
    ax.set_ylabel('Speed')
    ax.set_title('Time Series of Speed')
    
    # Set the tick labels on the x-axis with rotation
    x_ticks = pd.date_range(x['time21_5'].min(), x['time21_5'].max(), freq='MS')  # Create monthly tick positions
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_ticks.strftime('%Y-%m'), rotation=45)  # Format tick labels as 'YYYY-MM'
    
    ax.grid(True)
    plt.tight_layout()

    # Return the Matplotlib figure
    return fig

def heat_map(x, color_by):
    """
    Generate a heatmap depicting the average values based on the selected color_by parameter.

    This function generates a heatmap to visualize the average values based on the selected color_by parameter.
    The heatmap is organized by day of the week and month, displaying the average values of the selected parameter.

    Args:
        x (pandas.DataFrame): The input DataFrame containing time series data.
        color_by (str): The selected parameter to use for coloring the heatmap.

    Returns:
        matplotlib.figure.Figure: The Matplotlib figure containing the heatmap.
    """
    # Convert time21_5 column to datetime format
    x['time21_5'] = pd.to_datetime(x['time21_5'])
    
    # Bin the time21_5 column into 12 bins representing 12 weeks
    x['time21_5_bin'] = pd.cut(x['time21_5'], bins=12)
    
    # Map the day of the week to the corresponding integer value (0 - Monday, 1 - Tuesday, ..., 6 - Sunday)
    x['day_of_week'] = x['time21_5'].dt.dayofweek + 1  # Adjust day_of_week from 0-based to 1-based
    
    # Determine which column to use for coloring based on the selected value
    if color_by == 'speed':
        color_column = 'speed'
    elif color_by == 'longitude':
        color_column = 'longitude'
    elif color_by == 'latitude':
        color_column = 'latitude'
    
    # Pivot the DataFrame to get the heatmap data
    heatmap_data = x.pivot_table(index='day_of_week', columns='time21_5_bin', values=color_column, aggfunc='mean')
    
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
    plt.title(f'Heatmap of {color_by.capitalize()} (Average) by Month and Day of the Week')
    
    # Convert the plot to a Streamlit-friendly format and return it
    plt.tight_layout()
    return plt