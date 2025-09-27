import json


with open("data.json") as f:
    data = json.load(f)


g = [i for n, i in enumerate(data, start = 1) if n % 2==0]

print(len(g))