import donki_api_module
print(donki_api_module.__doc__)
# Call the function to download the data and store it in a dictionary of DataFrames
data_frames = donki_api_module.download_donki_data()

# Now you can work with the data stored in the data_frames dictionary
print(data_frames['FLR'])
