import donki_api_module

# Call the function to download the data and store it in a dictionary of DataFrames
data_frames = donki_api_module.download_donki_data()

# Now you can work with the data stored in the data_frames dictionary
for endpoint, df in data_frames.items():
    print(f'Data for endpoint {endpoint}:')
    print(df.head())  # Assuming you want to print the first few rows of each DataFrame
    print('\n')
