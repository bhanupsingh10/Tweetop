import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

def db_cursor():
	BASE_DIR = os.getcwd()
	print(BASE_DIR)
	print(os.path.join(BASE_DIR, "static", "cred.json"))
	cred = credentials.Certificate(os.path.join(BASE_DIR, "static", "cred.json"))
	firebase_admin.initialize_app(cred)
	db = firestore.client()
	return db
