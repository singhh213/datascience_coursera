DATA SCIENCE INDEPENDENT STUDY

<b>Assignment #1 : Twitter Sentiment Analysis in Python</b> <br>
Link to assignment: <a/>https://class.coursera.org/datasci-002/assignment/view?assignment_id=3</a>

Problem 1: Get Twitter Data <br>
Results: problem_1_submission.txt

Problem 2: Derive the sentiment of each tweet <br>
Run command: $ python tweet_sentiment.py AFINN-111.txt tweetstream.txt

Problem 3: Derive the sentiment of new terms <br>
Run command: $ python term_sentiment.py AFINN-111.txt tweetstream.txt

Problem 4: Compute Term Frequency <br>
Run command: $ python frequency.py tweetstream.txt

Problem 5: Which State is happiest? <br>
Run command: $ python happiest_state.py AFINN-111.txt tweetstream.txt

Problem 6: Top ten hash tags <br>
Run command: $ python top_ten.py tweetstream.txt
<br>
<br>


<b>Assignment #2 : Database Assignment: Simple In-Database Text Analytics</b> <br>
Link to assignment: <a>https://class.coursera.org/datasci-002/assignment/view?assignment_id=21</a>

Problem 1: Inspecting the Reuters Dataset; Basic Relational Algebra <br>
Run command: sqlite3 reuters.db < part1.sql

Problem 2: Matrix Multiplication in SQL (Express A X B as a SQL query) <br>
Run command: sqlite3 matrix.db < part2.sql

Problem 3: Working with a Term-Document Matrix <br>
-Write a query to compute the similarity matrix DDT  <br>
-Find the best matching document to the keyword query "washington taxes treasury". <br>
Run command: sqlite3 reuters.db < part3.sql

<br>
<br>
<b>Assignment #3 : Algorithms in MapReduce</b> <br>
Link to assignment: <a>https://class.coursera.org/datasci-002/assignment/view?assignment_id=5</a>

Problem 1: Create an Inverted index. <br>
Run command: $ python inverted_index.py data/books.json

Problem 2: Implement a relational join as a MapReduce query <br>
Run command: $ python join.py data/records.json

Problem 3: Describe a MapReduce algorithm to count the number of friends for each person. <br>
Run command: $ python friend_count.py data/friends.json

Problem 4: Generate a list of all non-symmetric friend relationships. <br>
Run command: $ python asymmetric_friendship.py data/friends.json

Problem 5: Write a MapReduce query to remove the last 10 characters from each string of nucleotides. <br>
Run command: $ python unique_trims.py data/dna.json
