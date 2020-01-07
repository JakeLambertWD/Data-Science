def trackVersionsJSON()

	import psycopg2
	import json

	connectstr = "dbname='musicbrainz_db' user='test_student' password='test_student' host='localhost'"
	conn = psycopg2.connect(connectstr)

	cursor = conn.cursor()
	cursor.execute("""SELECT DISTINCT r.name, a.name
	FROM recording r 
	JOIN track t ON r.id = t.recording
	JOIN artist_credit ac ON ac.id = t.artist_credit
	JOIN artist_credit_name an ON ac.id = an.artist_credit
	JOIN artist a ON a.id = an.artist
	JOIN artist_tag at ON a.id = at.artist
	JOIN tag tg ON tg.id = at.tag
	WHERE tg.name='deep house' 
	ORDER BY a.name ASC, r.name ASC
	LIMIT 100;
	""")

	rows = cursor.fetchall()
	result = []
	for row in rows:
		d = dict()
		d['Track Name'] = row[0]
		d['Artist'] = row[1]
		result.append(d)
			
	subjects = json.dumps(result, indent=2)
	print subjects
	
trackVersionsJSON() 
 


	
	

 