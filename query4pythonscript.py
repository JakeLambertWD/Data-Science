def releaseTypeXML();		
	
import psycopg2

connectstr = "dbname='musicbrainz_db' user='test_student'password='test_student' host='localhost'"
conn = psycopg2.connect(connectstr)

cursor = conn.cursor()
cursor.execute("""SELECT DISTINCT rp.name,  a.name , r.name , rc.date_year 
FROM artist a
JOIN artist_credit_name acn ON a.id = acn.artist
JOIN artist_credit ac ON ac.id = acn.artist_credit 
JOIN track t ON ac.id = t.artist_credit
JOIN release r ON r.artist_credit = ac.id
JOIN release_country rc ON r.id = rc.release
JOIN artist_tag at ON a.id = at.artist
JOIN tag tg ON tg.id = at.tag
JOIN release_group rg ON rg.id = r.release_group
JOIN release_group_primary_type rp ON rp.id = rg.type
AND tg.name='deep house' 
AND rc.date_year BETWEEN 2000 AND 2017
GROUP BY rp.name, r.name, rc.date_year, a.name
ORDER BY a.name
LIMIT 100;
""")
rows = cursor.fetchall()

print"<?xml version='1.0' encoding='UTF-8'?>"
print"<release_category>"

for row in rows:
	print("<release>")
	print("  <type>" + row[0] + "</type>")
	print("  <artist>" + row[1] + "</artist>")
	print("  <name>" + row[2] + "</name>")
	print("  <year> %i</year>" %row[3])
	print("</release>")
	 
print"</release_category>"
	
releaseTypeXML()