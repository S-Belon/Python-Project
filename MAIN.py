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

flr_avrg_365 = flr_df['duration'].mean()
flr_avrg_7 = flr_7['duration'].mean()
duration_diff = flr_avrg_7 - flr_avrg_365 # DASH
print("Duration Diff:", duration_diff)

flr_count_365 = len(flr_df) / 7
flr_count_7 = len(flr_7)
count_diff = flr_count_7 - flr_count_365 # DASH
print("Count Diff:", count_diff)

cme_df = data_frames['CMEAnalysis']
cme_7 = data_7['CMEAnalysis']

cme_avrg_365 = cme_df['speed'].mean()
cme_avrg_7 = cme_7['speed'].mean()
speed_diff = cme_avrg_7 - cme_avrg_365 # DASH
print("Speed Diff:", speed_diff)


graphs.flr_hist(flr_df)
graphs.flr_class(flr_df)
graphs.hist_CME_speed(cme_df)
graphs.flr_class_dist(flr_7) # DASH
