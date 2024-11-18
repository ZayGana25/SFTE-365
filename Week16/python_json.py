import json

data=["Student",{"Name":"Isaiah", "Age":23, "Sex":"Male", "ID:":20097}]
s = json.dumps(data)
print(s, type(s))

data = json.loads(s)
print(data, type(data))