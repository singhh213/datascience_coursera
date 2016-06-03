/* #1 σ10398_txt_earn(frequency) */
SELECT count(*) FROM (
	SELECT * FROM frequency WHERE docid='10398_txt_earn') x;

/* #2 πterm(σdocid=10398_txt_earn and count=1(frequency))*/
SELECT count(*) FROM (
	SELECT term FROM frequency WHERE docid='10398_txt_earn' AND count=1
) x;

/* #3 πterm(σdocid=10398_txt_earn and count=1(frequency)) U πterm(σdocid=925_txt_trade and count=1(frequency)) */
SELECT count(*) FROM (
	SELECT term FROM frequency WHERE docid='10398_txt_earn' AND count=1

UNION

	SELECT term FROM frequency WHERE docid='925_txt_trade' AND count=1
) x;

/* #4 Write a SQL statement to count the number of documents containing the word "parliament */
SELECT count(*) FROM (

	SELECT * FROM frequency WHERE term='parliament'
) x;

/* #5 Write a SQL statement to find all documents that have more than 300 total terms, including duplicate terms.  */
SELECT count(*) FROM (
	SELECT docid, sum(count) FROM frequency GROUP BY docid HAVING sum(count) > 300
) x;

/* #6 Write a SQL statement to count the number of unique documents that contain both the word 'transactions' and the word 'world'. */
SELECT count(distinct docid) FROM frequency WHERE docid in (SELECT docid FROM frequency WHERE term='transactions') AND term='world';



