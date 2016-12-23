
import json

file = open("sample.json", "w")
table = {'John': 123, 'Doe': 456, 'Mary': 789, 'Lisa': 123}

json.dump(table, file)
