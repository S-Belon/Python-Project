import pandas as pd

def flr_hist():
    # Find the index of the minimum value in the 'duration_minutes' column
    min_index = flr_df["duration"].idxmin()
    flr_df.iloc[min_index]
