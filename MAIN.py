import donki_api_data

print(donki_api_data.download_donki_data.__doc__)
# Call the function to download the data and store it in a dictionary of DataFrames
data_frames = donki_api_data.download_donki_data()

# Now we can work with the data stored in the data_frames dictionary
print(data_frames.keys())

from functions import solar_flare_df

print(solar_flare_df.__doc__)
solar_flare_df(data_frames)
flr_df = data_frames['FLR']
flr_df['duration'].describe()

import graphs
graphs.flr_hist(flr_df)
graphs.flr_class(flr_df)
