'''
checkout http://nodotcom.org/python-twitter-tutorial.html for more instructions
'''
import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "xxxxx",
    "consumer_secret"     : "xxxxx",
    "access_token"        : "xxxxx",
    "access_token_secret" : "xxxxx" 
    }

  api = get_api(cfg)

  # send tweet
  # tweet_1 = "this is a test tweet without pic"
  # status = api.update_status(status = tweet_1) 

  # send tweet with image
  photo_path = '../test.jpg'
  tweet_2 = "this is a test tweet with pic"
  api.update_with_media(photo_path, status = tweet_2)


if __name__ == "__main__":
  main()