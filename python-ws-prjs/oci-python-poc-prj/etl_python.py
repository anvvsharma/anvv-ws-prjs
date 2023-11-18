import pandas as pd
from datetime import datetime
# Set up the data streaming source (e.g. a CSV file)
input_file='C:/Users/VeerabhadraSharma/OneDrive - Accelalpha Software Pvt. Ltd/Documents/anvv-accel-2021/Projects/ADMC/Build/cpq/Item_master/test.csv'
now = datetime.now()

# Step 1: Extract the data from a CSV file
df = pd.read_csv(input_file)

# Step 2: Transform the data by adding a new column and converting the date format
df['Year'] = pd.to_datetime(df['MODEL_YEAR']).dt.year
# df['Year'] = '2023'
# Step 3: Load the transformed data into a new CSV file
df.to_csv('t_output.csv', index=False)
