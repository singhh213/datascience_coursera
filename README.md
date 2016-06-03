DATA SCIENCE INDEPENDENT STUDY

Assignment #1 : Twitter Sentiment Analysis in Python
Link to assignment: <a/>https://class.coursera.org/datasci-002/assignment/view?assignment_id=3</a>

Problem 1: Get Twitter Data
Results: problem_1_submission.txt

Problem 2: Derive the sentiment of each tweet
Run command: $ python tweet_sentiment.py AFINN-111.txt tweetstream.txt

Problem 3: Derive the sentiment of new terms
Run command: $ python term_sentiment.py AFINN-111.txt tweetstream.txt

Problem 4: Compute Term Frequency
Run command: $ python frequency.py tweetstream.txt

Problem 5: Which State is happiest?
Run command: $ python happiest_state.py AFINN-111.txt tweetstream.txt

Problem 6: Top ten hash tags
Run command: $ python top_ten.py tweetstream.txt



Assignment #2 : Database Assignment: Simple In-Database Text Analytics
Link to assignment: <a>https://class.coursera.org/datasci-002/assignment/view?assignment_id=21</a>

Problem 1: Inspecting the Reuters Dataset; Basic Relational Algebra
Run command: sqlite3 reuters.db < part1.sql

Problem 2: Matrix Multiplication in SQL (Express A X B as a SQL query)
Run command: sqlite3 matrix.db < part2.sql

Problem 3: Working with a Term-Document Matrix
-Write a query to compute the similarity matrix DDT 
-Find the best matching document to the keyword query "washington taxes treasury".
Run command: sqlite3 reuters.db < part3.sql



Assignment #3 : Algorithms in MapReduce
Link to assignment: <a>https://class.coursera.org/datasci-002/assignment/view?assignment_id=5</a>

Problem 1: Create an Inverted index.
Run command: $ python inverted_index.py data/books.json

Problem 2: Implement a relational join as a MapReduce query
Run command: $ python join.py data/records.json

Problem 3: Describe a MapReduce algorithm to count the number of friends for each person.
Run command: $ python friend_count.py data/friends.json

Problem 4: Generate a list of all non-symmetric friend relationships.
Run command: $ python asymmetric_friendship.py data/friends.json

Problem 5: Write a MapReduce query to remove the last 10 characters from each string of nucleotides.
Run command: $ python unique_trims.py data/dna.json






 



