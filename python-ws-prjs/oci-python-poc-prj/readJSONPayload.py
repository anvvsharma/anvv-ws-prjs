from pprint import pprint

import requests

# Set the API endpoint URL
# url = 'https://jsonplaceholder.typicode.com/posts/1'
#url = 'http://date.jsontest.com'
#url ='http://ip.jsontest.com/'
url = 'https://dummyjson.com/products/1'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    pprint(data)
    #print(data)
else:
    print('Error:', response.status_code)
