from django.shortcuts import render, render_to_response, redirect
import tweepy
from django.http import *
from django.urls import reverse, path

API_key = "TWITTER API KEY"
API_key_secret = "TWITTER API KEY SECRET"


def index_view(request):
	#print(request)
	if(checker(request)):
		#print("Path is: ", request.path)
		#print("Domain is: ", request.get_host())
		return redirect("http://" + request.get_host() + "/home") 	# Sending user diretly to home page is already logged In!
		#return path('home/', dashboard)
	else:
		return render_to_response("login.html")					# User Not logged In.


def checker(request):			# Checks wether there is correct secret as cokkies or not
	try:
		access_key = request.session.get('access_key', None)
		if not access_key:
			return False
	except KeyError:
		return False
	return True

def auth_view(request):
	OAuth = tweepy.OAuthHandler(API_key, API_key_secret)			# InitaliAIng our Oauth1 client
	redirect_url = OAuth.get_authorization_url()			# URL Generated where PIN Is
	response = HttpResponseRedirect(redirect_url)	
	
	#print(response)
	request.session['request_token'] = OAuth.request_token		# Saving the genrated token
	#print(OAuth.request_token)
	#return render("<h1>Hello</h1>")
	return response								#Sending the user to auth URL

def callback(request):
	pin = request.GET.get('pin')				# Getting PIN from get request
	oauth = tweepy.OAuthHandler(API_key, API_key_secret)
	token = request.session.get('request_token')		# Getting out token 
	request.session.delete('request_token')
	oauth.request_token = token
	#print("Token is", token)
	
	try:
		oauth.get_access_token(pin)				
		request.session['access_key'] = oauth.access_token			# Saving Auth keys for  future use.
		request.session['access_key_secret'] = oauth.access_token_secret
		api = tweepy.API(oauth)
		me = api.me()									# API connected!
		#print(me.screen_name)
	except:
		print("Error Occured at views 43!")
	
	return redirect("http://" + request.get_host())			# Sending user to index view.
#
# return render(request,'index_view', {})
	#return render(request,'home.html',{})
#print(acess_token, acess_token_secret)

# Create your views here.
