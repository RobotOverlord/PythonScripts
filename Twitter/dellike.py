import tweepy
import csv

consumer_key = 'g1dFP8fkMUdsVzI0KNyo6cZ2a'
consumer_secret = '3tgsVN2Ny0b3qecsOfYWxM3Jvfii092GAoDR0XVn1VuRGU2sdF'
access_key = '13092332-L1CThQnkmQqfHKYafOGWQAMrTpBXWn3X37IfH9qQ1'
access_secret = 'z5AA3L0vWFds8ipMX5p7nW66QJGPDemPITf38x4zoCi81'

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

likes = tweepy.Cursor(api.favorites, count=200).items()

while True:
	tweet = likes.next()
	api.destroy_favorite(tweet.id_str)

