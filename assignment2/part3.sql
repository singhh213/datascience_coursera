/* Problem H */
SELECT A.docid, B.docid, SUM(A.count * B.count)
FROM frequency as A join frequency as B on A.term = B.term
WHERE A.docid < B.docid
AND A.docid = '10080_txt_crude'
AND B.docid = '17035_txt_earn'
GROUP BY A.docid, B.docid;

/* Problem I */

CREATE VIEW Z AS
SELECT * FROM frequency 
UNION 
SELECT 'q' as docid, 'washington' as term, 1 as count
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION
SELECT 'q' as docid, 'treasury' as term, 1 as count;

SELECT B.docid, SUM(A.count * B.count)
FROM 
(SELECT docid, term, count FROM Z WHERE docid='q') AS A 
JOIN frequency AS B ON A.term = B.term
GROUP BY B.docid
ORDER BY SUM(A.count * B.count) desc limit 10;



