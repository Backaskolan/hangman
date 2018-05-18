import json
from collections import OrderedDict

with open('scores.json', 'r') as f:
		scores = json.load(f)
	
for r in sorted(scores, key=lambda t: t['highest_round'], reverse=True):
	print('{}\t\t{}\t\t{}\t\t{}'.format(r['player_name'], r['highest_round'], r['lives'], r['difficulty']))