import json

dict = {"Python": '.py', 'Java': '.java', 'C++': '.cpp'}

json = json.dumps(dict, sort_keys=True, indent=4)
f = open("dict.json", "w")
f.write(json)
f.close()
