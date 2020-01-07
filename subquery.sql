SELECT sub1.country "Country", sub1.cnt "Total Artists", sub2.cnt "Total Labels"
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