import donki_api_data

print(donki_api_data.download_donki_data.__doc__)
# Call the function to download the data and store it in a dictionary of DataFrames
data_frames = donki_api_data.download_donki_data()

# Now you can work with the data stored in the data_frames dictionary
print(data_frames.keys())

import functions

print(functions.solar_flare_df.__doc__)
functions.solar_flare_df(data_frames)
# flr_df['duration'].describe()
