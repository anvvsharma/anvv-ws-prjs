import csv
from datetime import datetime

import pandas as pd

input_file='C:/Users/VeerabhadraSharma/OneDrive - Accelalpha Software Pvt. Ltd/Documents/anvv-accel-2021/Projects/ADMC/Build/cpq/Item_master/test.csv'
now = datetime.now()

chunksize = 10**6  # Set chunk size to 1 million rows

for chunk in pd.read_csv(input_file, chunksize=chunksize, lineterminator='\n'):
    # Process each chunk
    processed_chunk = chunk
    processed_chunk.to_csv("test_1.csv", header=True, index=False)
    print(chunk)
