def artistGenreJSON():

	import psycopg2
	import json

	connectstr = "dbname='musicbrainz_db' user='test_student' password='test_student' host='localhost'"
	conn = psycopg2.connect(connectstr)

	cursor = conn.cursor()
	cursor.execute("""SELECT DISTINCT a.name, t.name, t.ref_count 
	FROM artist_tag at 
	JOIN artist a ON a.id = at.artist  
	JOIN tag t ON t.id = at.tag  
	WHERE t.name='deep house'
	ORDER BY a.name
	LIMIT 100;
	""")

	rows = cursor.fetchall()
	result = []
	for row in rows:
		d = dict()
		d['Artist'] = row[0]
		d['Genre'] = row[1]
		d['Ref Count'] = str(row[2])
		result.append(d)
		
	subjects = json.dumps(result, indent=4)
	print subjects
	
artistGenre() 
 