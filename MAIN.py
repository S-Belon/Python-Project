import donki_api_data
import functions
import graphs

print(donki_api_data.download_donki_data.__doc__)
# Call the function to download the data and store it in a dictionary of DataFrames
data_frames = donki_api_data.download_donki_data()
data_7 = donki_api_data.data_7()
print(data_frames.keys())


flr_df = data_frames['FLR']
flr_7 = data_7['FLR']

print(functions.flr_duration.__doc__)
functions.flr_duration(flr_df)
functions.flr_duration(flr_7)

flr_df['duration'].describe()
flr_7['duration'].describe()

avrg_365 = flr_df['duration'].mean()
print("Average:", avrg_365)
recent_diff = flr_7['duration'].mean() - avrg_365
print("Diff:", recent_diff)

cme_df = data_frames['CMEAnalysis']


graphs.flr_hist(flr_df)
graphs.flr_class(flr_df)
graphs.hist_CME_speed(cme_df)
