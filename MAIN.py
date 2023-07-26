import donki_api_data
import functions
import graphs

print(donki_api_data.download_donki_data.__doc__)
# Call the function to download the data and store it in a dictionary of DataFrames
data_frames = donki_api_data.download_donki_data()

# Now we can work with the data stored in the data_frames dictionary
print(data_frames.keys())

flr_df = data_frames['FLR']

print(dir(functions))

print(functions.flr_duration.__doc__)
functions.flr_duration(flr_df)

flr_df['duration'].describe()
cme_df = data_frames['CMEAnalysis']


graphs.flr_hist(flr_df)
graphs.flr_class(flr_df)
graphs.hist_CME_speed(cme_df)
