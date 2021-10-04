# This is a collection of project2  

(a) Explore Twitter APIs  
----------------------------
## function 1: Get All Informatioin of Tweets From One User's Twitter  
This code is designed to get a certain number（ `200` is the `maximum allowed count` ) of latest tweets from a `specified user`.  
* I download ten tweets from Taylor Swift's Twitter  
* The obtained file format is **.json**  
* The file contains all the information on the user’s Twitter homepage, including username, nickname, account establishment time, profile, number of friends, etc.  
--------------------
## function 2: Get Text from One User's Twitter  
This code is designed to `only` obtain `text messages` from one user's tweets.  

--------------------
(b) Explore Google NLP APIs  
------------------------------
## Analyze sentiment in a string  
This program is written to inspect the given text and identify the prevailing emotional opinion.
* from the result, we can not only see the given text but also see sentiment with two parameters.
* parameter 1: `score` -- ranging from -1.0 ( negative sentiment) to 1.0 ( positive sentiment). 
* parameter 2:`magnitude` -- a non-negative number ranging from 0 to +inf, which represents the absolute magnitude of sentiment no matter score is negative or positive.
