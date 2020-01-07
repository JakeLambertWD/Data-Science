def releaseYearJSON();

	import psycopg2
	import json

	connectstr = "dbname='musicbrainz_db' user='test_student' password='test_student' host='localhost'"
	conn = psycopg2.connect(connectstr)

	cursor = conn.cursor()
	cursor.execute("""SELECT DISTINCT a.name, r.name, t.name, rc.date_year
	FROM artist a
	JOIN artist_credit_name acn ON a.id = acn.artist
	JOIN artist_credit ac ON ac.id = acn.artist_credit 
	JOIN track t ON ac.id = t.artist_credit
	JOIN release r ON r.artist_credit = ac.id
	JOIN release_country rc ON r.id = rc.release
	JOIN artist_tag at ON a.id = at.artist
	JOIN tag tg ON tg.id = at.tag
	AND tg.name='deep house' 
	AND rc.date_year BETWEEN 2000 AND 2017
	GROUP BY r.name, t.name, rc.date_year, a.name
	ORDER BY a.name ASC
	LIMIT 100;
	""")

	rows = cursor.fetchall()
	result = []
	for row in rows:
		d = dict()
		d['Artist'] = row[0]
		d['Release'] = row[1]
		d['Title'] = row[2]
		d['Year'] = str(row[3])
		result.append(d)
				
	subjects = json.dumps(result, indent=4)
	print subjects
	
releaseYearJSON() 
 