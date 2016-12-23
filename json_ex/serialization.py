
import json

file = open("sample.json", "w")
table = {'Mircea': 123, 'Sorina': 456, 'Ilinca': 789, 'Lia': 123}

json.dump(table, file)
