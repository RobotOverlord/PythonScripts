import tweepy
import csv

"""Authenticate with twitter using OAuth"""

def read_csv(file):
    """
    reads a CSV file into a list of lists
    """
    with open(file, encoding = 'utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        rows = []
        for line in reader:
            row_data = []
            for element in line:
                row_data.append(element)
            if row_data != []:
                rows.append(row_data)
    rows.pop(0)
    return(rows)

def oauth_login(consumer_key, consumer_secret):
    """Authenticate with twitter using OAuth"""
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth_url = auth.get_authorization_url()
    verify_code = raw_input("Authenticate at %s and then enter you verification code here > " % auth_url)
    auth.get_access_token(verify_code)
    return tweepy.API(auth)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
print("Authenticated as: %s" % api.me().screen_name)

tweets = read_csv('originaltweets.csv')

tweets_marked = []
month_list = ['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']
hashtag = 'http'

for tweet in tweets:
    if hashtag in tweet[5]:
        if tweet[3][0:4] in month_list:
            tweets_marked.append(tweet)

print(len(tweets_marked), 'tweets marked for deletion.')

# build list of marked status IDs
to_delete_ids = []
delete_count = 0
for tweet in tweets_marked:
    to_delete_ids.append(tweet[0])

# delete marked tweets by status ID
for status_id in to_delete_ids:
    try:
        api.destroy_status(status_id)
        print(status_id, 'deleted!')
        delete_count += 1
    except:
        print(status_id, 'could not be deleted.')
print(delete_count, 'tweets deleted.')