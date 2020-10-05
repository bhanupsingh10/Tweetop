from django.shortcuts import render
import tweepy
from .utils import get_Api
from .models import TweetData
from django.utils import timezone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
from dateutil import parser
import datetime
from datetime import date
import re
from heapq import nlargest
from users.views import index_view

# Create your views here.

def url_filter(my_tweets): 		# Returns only tweets with links
	filtered_data = []
	for tweet in my_tweets:
		if(len(tweet.entities['urls'])!=0):
			filtered_data.append(tweet)
	return filtered_data

def date_filter(my_tweets):		# Return tweets of past 7 days!
	filtered_data = []
	d2 = str(datetime.date.today())
	d2 = date(int(d2[0:4]),int(d2[5:7]),int(d2[8:10]))
	for tweet in my_tweets:
		d1 = str(parser.parse(str(tweet.created_at)))
		d1 = d1[0:10]
		d1 = date(int(d1[0:4]),int(d1[5:7]),int(d1[8:10]))
		D = d2 - d1
		if(int(D.days)<7):
			filtered_data.append(tweet)
		else:
			break
	return filtered_data

def get_data(request):
	api = get_Api(request)
	BASE_DIR = os.getcwd()
	print(BASE_DIR)
	try:
		firebase_admin.get_app()
	except ValueError as e:
		cred = credentials.Certificate(os.path.join(BASE_DIR,"tweet", "static", "cred.json"))
		firebase_admin.initialize_app(cred)
	
	db = firestore.client()
	doc_ref = db.collection('users').document('data')
	#print(api)
	me = api.me()
	frnds = api.friends()
	users_list = []
	for f in frnds:
		users_list.append(f.screen_name)
	users_list.append(me.screen_name)
	#print(users_list)
	full_data = []
	trending_user = {}
	trending_url = {}
	for uid in users_list:
		my_tweets = api.user_timeline(uid, count=10)			# Getting User Tweets
		my_tweets = url_filter(my_tweets)					# Filtering tweets wih links
		my_tweets = date_filter(my_tweets)				# Filtering tweets of past 7 days
		trending_user[uid] = len(my_tweets)
		#print(len(my_tweets))
		for tweets in my_tweets:
			my_tweet_text = tweets.text
			user_name = tweets.user.name
			dp_url = tweets.user.profile_image_url_https
			my_dict = {
				'Name': user_name,
				'tweet' : my_tweet_text,
				'created_date' : tweets.created_at,
				'url' : tweets.entities['urls'][0]['expanded_url'],
				'dp_url': dp_url
			}
			doc_ref.collection(uid).document(tweets.id_str).set(my_dict)
			full_data.append(my_dict)
			url = my_dict['url']
			result = re.sub(r'(.*://)?([^/?]+).*', '\g<1>\g<2>', url)
			if result in trending_url.keys():
				trending_url[result]+=1
			else:
				trending_url[result] = 0
	
	return full_data, trending_url, trending_user

def dashboard(request):
	my_data, trending_url, trending_user = get_data(request)
	top_link = nlargest(3, trending_url, key = trending_url.get)
	top_user = nlargest(3, trending_user, key = trending_user.get)

	return render(request, 'home.html', {'data':my_data, 'links':top_link, 'users':top_user})

def logout(request):
	request.session['access_key']=None
	request.session['access_key_secret']=None
	return index_view(request)


