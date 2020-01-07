import psycopg2
connectstr = "dbname='musicbrainz_db' user='test_student' password='test_student' host='localhost'" 
conn = psycopg2.connect(connectstr) 
cursor = conn.cursor() 
cursor.execute("""SELECT sub1.country "Country", sub1.cnt "Total Artists", sub2.cnt "Total Labels"
FROM(SELECT COUNT(a.id) as cnt, ar.name as country 
  FROM artist a JOIN area ar ON  ar.id = a.area 
  JOIN area_type at ON at.id = ar.type
  WHERE at.name = 'Country' 
  GROUP BY ar.name) as sub1,
(SELECT COUNT(l.id) as cnt, ar.name as country
  FROM area ar JOIN label l ON  ar.id = l.area  
  JOIN area_type at ON at.id = ar.type
  WHERE at.name = 'Country'
  GROUP BY ar.name
  ORDER BY ar.name) as sub2
WHERE sub1.country = sub2.country;
""") 
rows = cursor.fetchall() 

f = open("countries.csv", "w")

f.write("Country, No. Artists, No. Labels\n")
for row in rows:
	 f.write("%s, %i, %i\n" %(row[0] ,  row[1]  ,  row[2]))
f.close()
