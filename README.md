# Space Weather Dashboard
A Streamlit-based dashboard that provides insights into space weather using data from NASA's API. The dashboard focuses on daily updates about solar activities such as solar flares and provides comparison between recent data and weekly averages over the past 365 days. 

## Features
- **Daily Updates**: The dashboard is designed to change daily, pulling data from the last 365 days.
- **7-day Comparison**: Compare the most recent 7 days of data with the weekly average of the past 365 days.
- **Modular Design**: Code is structured using modules for better organization.

## Installation
1. Clone the repository.
2. Install the required packages using:
   ```
   pip install -r requirements.txt
   ```
3. Create a private key for using the NASA API [here](https://api.nasa.gov/).
4. In the cloned repository create a ``` .env ``` file. In this file you ought to store the obtained API key as follows:
   ```
   api_key=YOUR_API_KEY
   ```
5. Run the dash_app.py script to start the Streamlit server in your terminal:
   ```
   streamlit run dash_app.py
   ```

## Usage
Navigate to the URL provided by Streamlit (usually `http://localhost:8501`) in your browser to access the dashboard.

```
sanderbelon
├── data
│   ├── donki_api_data.py
├── src
│   ├── dash_app.py
│   ├── functions.py
│   ├── graphs.py  
├── eval
│   ├── README.md
├── docs
│   ├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
└── README.md
```

## Dashboard Insights
- **Metrics**:
   - *Solar Flare Duration*:
        - Representation: Average duration (in minutes) of solar flares in the selected time period.
        - Significance: Indicates the average duration of solar flares, which can provide insights into the intensity and impact of solar activity.

   - *Solar Flare Count*:
        - Representation: Total count of solar flares in the selected time period.
        - Significance: Reflects the frequency of solar flares, which can indicate the overall solar activity level.

   - *CME Speed*:
        - Representation: Average speed of Coronal Mass Ejections (CMEs) in kilometers per second (km/s).
        - Significance: Represents the speed at which CMEs, massive solar eruptions, propagate through space. Faster CMEs can have greater impacts on Earth's space environment.

- **Charts**:

   - *Heatmap*:
        - Representation: A heatmap displaying the average value of a selected parameter (color-coded) across different days of the week and months.
        - Significance: Provides an overview of how a specific space weather parameter (e.g., speed, longitude, or latitude) varies over the course of a week and different months. Patterns and trends can be identified.

   - *Donut Chart*:
        - Representation: A donut chart illustrating the distribution of solar flare class types.
        - Significance: Visualizes the composition of solar flare classes, helping to understand the occurrence of different types of solar flares.

   - *Line Chart - Half Angle, Latitude, Longitude*:
        - Representation: Time series line chart showing changes in half angle, latitude, and longitude of solar events over time.
        - Significance: Demonstrates how certain solar event characteristics evolve over the selected time period. Patterns and correlations can be observed.

   - *Line Chart - CME Speed*:
        - Representation: Time series line chart depicting changes in CME speeds over time.
        - Significance: Illustrates the variation in CME speeds, helping to identify trends and anomalies in solar eruption velocities.

## Author
- **Sander Belon**

## Requirements
- Python 3.7 or higher
- Streamlit
- Any other specific packages or libraries used specified in requirements.txt

`

