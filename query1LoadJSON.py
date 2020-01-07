import json
data = json.load("artists.json")

for a in data['artist_collection']:
	db.artists.insert(a)