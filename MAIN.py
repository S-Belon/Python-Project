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

avrg_365 = flr_df['duration'].mean()
avrg_7 = flr_7['duration'].mean()
duration_diff = avrg_7 - avrg_365 # DASH
print("Duration Diff:", duration_diff)

count_365 = len(flr_df) / 7
count_7 = len(flr_7)
count_diff = count_7 - count_365 # DASH
print("Count Diff:", count_diff)

cme_df = data_frames['CMEAnalysis']


graphs.flr_hist(flr_df)
graphs.flr_class(flr_df)
graphs.hist_CME_speed(cme_df)
