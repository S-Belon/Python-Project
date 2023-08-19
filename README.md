# Space Weather Dashboard
A Streamlit-based dashboard that provides insights into space weather using data from NASA's API. The dashboard focuses on daily updates about solar activities such as solar flares and provides comparison between recent data and weekly averages over the past 365 days. 

## Features
- **Daily Updates**: The dashboard is designed to change daily, pulling data from the last 365 days.
- **7-day Comparison**: Compare the most recent 7 days of data with the weekly average of the past 365 days.
- **Histogram**: View a histogram that illustrates the distribution of the number of events per month.
- **Modular Design**: Code is structured using modules for better organization.

## Installation
1. Clone the repository.
2. Install the required packages using:
   ```
   pip install -r requirements.txt
   ```
3. Run the main script to start the Streamlit server:
   ```
   streamlit run main.py
   ```

## Usage
Navigate to the URL provided by Streamlit (usually `http://localhost:8501`) in your browser to access the dashboard.

```
sanderbelon/Rafiga
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

## Contributing
- **Sander Belon**: Responsible for connecting the data to the dashboard and building the analysis tools.
- **Rafiga**: Responsible for the README file and other documentation.

## Requirements
- Python 3.7 or higher
- Streamlit
- Any other specific packages or libraries used

## Known Issues
- README file is still being finalized.
- Integration of some examples into MAIN.py is in progress.

## Grading Criteria
The final project will be assessed based on the following criteria:
- **Runability**: The code should execute without errors.
- **Organization**: The code and project files should be well-organized.
- **Appearance**: The dashboard should be visually appealing.
- **Added Value**: The insights provided by the dashboard should be valuable and informative.
- **Understanding of Course Materials**: The project should illustrate a clear grasp of the materials covered in the course.

## License
MIT

`

