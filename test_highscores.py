import json

with open('scores.json', 'r') as f:
		scores = json.load(f)
	
print(scores)