import pandas as pd
from datetime import datetime
import csv
# Set up the data streaming source (e.g. a CSV file)
input_file='C:/Users/VeerabhadraSharma/OneDrive - Accelalpha Software Pvt. Ltd/Documents/anvv-accel-2021/Projects/ADMC/Build/cpq/Item_master/ITEM_MASTER.csv'
now = datetime.now()

# Read the CSV file into a pandas DataFrame object
df = pd.read_csv(input_file)

# Create an empty dictionary to store the data for each column
columns = {}

# Iterate over the column names and extract the data for each column
for col in df.columns:
    columns[col] = df[col].tolist()
    for n in columns[col]:
        # print(col, ' = ', n)
# Convert the dictionary to a DataFrame object
new_df = pd.DataFrame(columns)

# Save the new DataFrame to a CSV file
new_df.to_csv('t_output.csv', index=False)
