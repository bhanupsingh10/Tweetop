import tweepy

API_key = "ohUSPDNOE5qc1X063SudPPCy9"
API_key_secret = "UnQJaovLV1PLBpqCDQaM5oKj6K0d2nEFbGOl11VTPScxmICiEE"

def get_Api(request):
	oauth = tweepy.OAuthHandler(API_key, API_key_secret)
	token = request.session.get('request_token')
	oauth.request_token = token
	oauth.access_token = request.session['access_key']
	oauth.access_token_secret = request.session['access_key_secret']
	api = tweepy.API(oauth)
	return api	
