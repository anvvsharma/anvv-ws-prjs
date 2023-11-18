import pandas as pd
from datetime import datetime
# Set up the data streaming source (e.g. a CSV file)
input_file='C:/Users/VeerabhadraSharma/OneDrive - Accelalpha Software Pvt. Ltd/Documents/anvv-accel-2021/Projects/ADMC/Build/cpq/Item_master/test.csv'
now = datetime.now()

# dd/mm/YY H:M:S
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("1. Entered Process - date and time =", now.strftime("%d/%m/%Y %H:%M:%S"))
stream = pd.read_csv(input_file, chunksize=100000, low_memory=False)

# Define a function to process each chunk of data
def process_data(chunk):
    result = chunk.groupby('LOCATION_CODE').sum()
    return result

# Iterate over each chunk of data and process it using the process_data() function
for chunk in stream:
    print("1. Enterted - date and time =", now.strftime("%d/%m/%Y %H:%M:%S"))
    processed_chunk = chunk
    print("2. Writing Data - date and time =", now.strftime("%d/%m/%Y %H:%M:%S"))
    processed_chunk.to_csv('t_processed_data.csv', header=True, index=False)
    print("3. Completed Writing - date and time =", now.strftime("%d/%m/%Y %H:%M:%S"))
