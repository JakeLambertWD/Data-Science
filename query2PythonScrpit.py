def trackVersionsXML();	
	
import psycopg2

connectstr = "dbname='musicbrainz_db' user='test_student'password='test_student' host='localhost'"
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

print"<?xml version='1.0' encoding='UTF-8'?>"
print"<remix_collection>"

for row in rows:
 print("<recording>")
 print("  <track name>" + row[1] + "</track name>")
 print("  <artist>" + row[0] + "</artist>")
 print("</recording>")

print"</remix_collection>"
	
trackVersionsXML()