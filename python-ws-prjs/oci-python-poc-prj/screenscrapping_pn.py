import pandas as pd

url = 'https://www.example.com'
data = pd.read_csv(url)

print(data.head())
