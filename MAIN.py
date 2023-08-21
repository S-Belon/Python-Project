import donki_api_data
import functions

data_frames = donki_api_data.download_donki_data()
data_7 = donki_api_data.data_7()

flr_df = data_frames['FLR']
flr_7 = data_7['FLR']

functions.flr_duration(flr_df)
functions.flr_duration(flr_7)

flr_avrg_365 = flr_df['duration'].mean()
flr_avrg_7 = flr_7['duration'].mean()
duration_diff = flr_avrg_7 - flr_avrg_365 

flr_count_365 = len(flr_df) / 7
flr_count_7 = len(flr_7)
count_diff = flr_count_7 - flr_count_365 

cme_df = data_frames['CMEAnalysis']
cme_7 = data_7['CMEAnalysis']

cme_avrg_365 = cme_df['speed'].mean()
cme_avrg_7 = cme_7['speed'].mean()
speed_diff = cme_avrg_7 - cme_avrg_365 

weekly_averages = functions.weekly_averages(cme_df)
