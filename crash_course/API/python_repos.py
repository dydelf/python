"""
Writing an api requests and processing data within.
"""

import requests
import json
import pygal

# make an API call and save the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code: ", r.status_code)

# Store API response in a variable
response_dict = r.json()
print("Total repos: ", response_dict['total_count'])

# Explore information about the repositories
repo_dicts = response_dict['items']
#print("Repositories returned: ", len(repo_dicts))

# Examine the first repository
#repo_dict = repo_dicts[0]
#print("\nKeys: ", len(repo_dict))
#for key in sorted(repo_dict.keys()):
#    print(key)
#for repo_dict in repo_dicts:
#    print("\n\nSelected information about the repository: ")
#    print('Name: ', repo_dict['name'])
#    print("Owner: ", repo_dict['owner']['login'])
#    print("Stars: ", repo_dict['stargazers_count'])
#    print("Repository: ", repo_dict['html_url'])
#    print("Created: ", repo_dict['created_at'])
#    print("Updated: ", repo_dict['updated_at'])
#    print("Description: ", repo_dict['description'])

# Saving data to file straight from request
#file = open("data.json", "w")
#file.write(r.text)
#file.close()

# Saving data to file after processing
#json = json.dumps(repo_dicts, indent=4)
#dict = open("dict_data2.json", "w")
#dict.write(json)
#dict.close()

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Make a visualisation
chart = pygal.Bar(x_label_rotation=45, show_legend=False)
chart.title = 'Most starred Python projects on GitHub'
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')
