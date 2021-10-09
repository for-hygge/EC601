#1 Explore Twitter APIs
====================
## function 1: Get Tweets From One User's Twitter
This code is designed to get a certain number（ `200` is the `maximum allowed count` ) of latest tweets from a `specified user`.  
* The obtained file format is **.json**
* The file contains all the information on the user’s Twitter homepage, including username, nickname, account establishment time, profile, number of friends, etc.
--------------------
## function 2:Search tweets with a given query
This code is designed to look for tweets posted by a user which contain a given keyword. 
The format of the file is also **.json**

--------------------
#2 Explore Goggle NLP APIs
============================
## test : Analyze sentiment in a string
This code is designed to analyze whether the sentiment in a string is positive or negative and also tell the language of the text.
* The text is "I am very sad." 
Sentence sentiment score: -0.8999999761581421
Sentence sentiment magnitude: 0.8999999761581421
Language of text is: en (which means ENGLISH)
* `score` ranges from -1 (negative) to +1 (positive). a score less than 0 up to -1 implies negative emotion and a score more than 0 up to +1 implies positive emotions.
* `magnitude` is used to measure the amount of emotional content found in the text. Its value can range from 0 to infinity.

#3 Social media analyzer
========================
* MVP: A product that can help us manage our emotion by analyzing our tweets during a given period.
* User storys: It is important to learn to control our emotions. This product can capture the tweets posted by users within a week to analyze whether their sentiment this week is more positive or negative, so that users can know themselves better and learn to control their emotion later.
* Modular design: First, this program uses Twitter API to get the tweets posted by a given user within a week. Then, it uses Google NLP API to analyze the sentiment. Finally, it records the results and give a feedback to the user.
* Users: All people who want to know themselves better and manage their emotion.
