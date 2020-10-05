import tweepy

API_key = "YOUR API KEY"
API_key_secret = "YOUR API KEY SECRET"

def get_Api(request):			# Returns our tweepy api handler
	oauth = tweepy.OAuthHandler(API_key, API_key_secret)
	token = request.session.get('request_token')
	oauth.request_token = token
	oauth.access_token = request.session['access_key']
	oauth.access_token_secret = request.session['access_key_secret']
	api = tweepy.API(oauth)	
	return api							
