import tweepy
import datetime
from google.cloud import language_v1

# Instantiates a client
client = language_v1.LanguageServiceClient.from_service_account_json('')

# case 1:input the wrong key and access, the output should be 401
# input access information
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
auth.set_access_token(access_key, access_secret)

# calling the api
api = tweepy.API(auth)

# case2: input a user name which does not exist
# the screen_name of the targeted user
name = "/./,/-"  # set your account screen name
score = 0  # initial score is 0
count = 0

now_time = datetime.datetime.now()
week_ago = datetime.timedelta(days=7)
all_tweets = []
new_tweets = api.user_timeline(screen_name=name, end_time=(week_ago-now_time).date(), start_time=now_time)
all_tweets.extend(new_tweets)

if all_tweets != []:
    for i in range(len(all_tweets)):
        document = language_v1.Document(content=all_tweets, type_=language_v1.Document.Type.PLAIN_TEXT)
        sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
        score = score + sentiment.score
        count = count + 1

if count !=0:
    avescore = score/count
    if avescore > 0:
        print('Your avescore is {} in the last week. You are in a good mood.', avescore)
    else:
        print('Your avescore is {} in the last week. You are in a bad mood.', avescore)
else:
    print('This user may not exist or post anything.')
    
# case3: test function
#all_tweets = ["I'm very happy","bad day","I like the weather","I watched a movie today"]
#if all_tweets != []:
#    for i in range(len(all_tweets)):
#        document = language_v1.Document(content=all_tweets, type_=language_v1.Document.Type.PLAIN_TEXT)
#        sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
#        score = score + sentiment.score
#        count = count + 1
#
#if count !=0:
#    avescore = score/count
#    if avescore > 0:
#        print('Your avescore is {} in the last week. You are in a good mood.', avescore)
#    else:
#        print('Your avescore is {} in the last week. You are in a bad mood.', avescore)
#else:
#    print('This user may not exist or post anything.')
