"""
This module provides functions for visualizing the space weather data.

Functions:
- flr_hist(x): Create a histogram of solar flare duration without outliers.

"""
import matplotlib.pyplot as plt

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