"""
Simple file to test the library requests.
"""

import requests
import json

# taking a request from github API which is modified with params
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)

# printing status code succesful or not
print(response.status_code)

# converting response into dictionary and json format
dict = response.json()

# printing headers of the response
headers = response.headers

# saving the dictionary response into the json file
json = json.dumps(dict, indent=4)
f = open("gitapi.json", "w")
f.write(json)
f.close()


