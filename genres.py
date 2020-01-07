import psycopg2
connectstr = "dbname='musicbrainz_db' user='test_student' password='test_student' host='localhost'" 
conn = psycopg2.connect(connectstr) 
cursor = conn.cursor() 
cursor.execute("""SELECT sub1.genre "Genre", sub1.cnt "Total Artist", sub2.cnt "Total Labels"
FROM(SELECT COUNT(a.id) as cnt, tg.name as genre 
FROM artist a
JOIN artist_tag at ON a.id = at.artist
JOIN tag tg ON tg.id = at.tag
GROUP BY tg.name
ORDER BY cnt DESC
LIMIT 100) as sub1,
(SELECT COUNT(l.id) as cnt, tg.name as genre
FROM label l 
JOIN label_tag lt ON l.id = lt.label
JOIN tag tg ON tg.id = lt.tag
JOIN label_type la ON la.id = l.type
GROUP BY tg.name
ORDER BY cnt DESC) as sub2
WHERE sub1.genre = sub2.genre
ORDER BY sub1.cnt DESC
LIMIT 100;
""") 
rows = cursor.fetchall() 

f = open("genres.csv", "w")

f.write("Genre, No. Artists, No. Labels\n")
for row in rows:
	 f.write("%s, %i, %i\n" %(row[0] ,  row[1]  ,  row[2]))
f.close()
