# Tweetop

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Tweetop is a webbased app which aims to collect tweets which contains links from user stream i.e user tweets and user's friends tweet of the past 7 days. Once fetched and stored in a database, the app should:
  - Display Actual Tweets containing links
  - Display Which user has shared the most links
  - Display List of Top Domains that have been shared so far

### Tech Stack

```
- Programming Languages
    - Python 3.6
- Frameworks
    - Django 2.2.4
- Database
     - Google Firebase Firestore
- Frontend
    - HTML 5
    - CSS 3
    - Bootstrap 4
- API
    - Tweepy Api
```

### Installation

Install the dependencies and devDependencies and start the server.
Note: Python must be installed on your system with versions 3.0 or above.
```sh
$ cd tweetop
$ pip install -r requirements.txt
$ python manage.py runserver
```
Browse to http://127.0.0.1:8000/ to see the local deployement.

### Deployement

The app is live and deployed to http://tweettop.herokuapp.com 

### Database Structure and Schema
 As Google Firebase is used as database for this app, the database is divided into documents and collections.
 Here's a hierarcy of the database:
```bash
DATABASE HIRERARCY
|---users
|--- |---data
|--- |--- |--- twitter user_name
|--- |--- |--- |--- |--- Tweet1
|--- |--- |--- |--- |--- Tweet2
|--- |--- |--- |--- |--- Tweet3
|--- |--- |--- |--- |--- ...

```
For every tweet the Schema is defined as follows
```bash
{
    'Name': "Actual Name of USER",
    'created_date': "TIMESTAMP of date of tweet",
    'dp_url': "URL of the User profile photo",
    'tweet': "Actual text of tweet",
    'url': "URL that is contained in the tweet"
}
```
### A Glimpse into the Backend
The backend of this app is managed by Django and Python. Tweepy API connects to the twitter's account of the user. Once connected the API fetches all the tweets of the user along with that of his/her friends. Then as clients requirement only tweets within the past 7 days are required , so a filtering function is used for that purpose. Moreover only those tweets are required which have links assosated with them, so second filter mechanism filter those tweets which have links.
So finally we are left with the required tweets of the user. Same process goes for users friends as well and we are left with the tweets that have to be displayed on the user's dashboard. Now every tweet list length of the user, gives details about the user's activity of that week and links shared by user along with his/her friends gives detail about the trending links. These are actually counted through a dictionary which makes this opeartion less costly.
Now we are requred to give top users and top links and for this app we are showing top 3 on both. A heap is used for that which given us top 3 users who shared most links and also top 3 trending links . Please not for links we are considering only domain names not exacty where the links refers.
Finally our data collection is done, and we save that data to our firebase server and display that data on or web site.


