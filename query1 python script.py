def artistGenreXML();

import psycopg2

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

print"<?xml version='1.0' encoding='UTF-8'?>"
print"<artist_collection>"

for row in rows:
	print("  <artist>")
	print("    <name>" + row[0] + "</name>")
	print("    <genre>" + row[1] + "</genre>")
	print("    <ref count> %i</ref count>" %row[2])
	print("  </artist>")
	
print("</artist_collection>")	
	
artistGenreXML() 
 