import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dbbee90776a3347a19c08a7ceec8d4ed')
    # Path to your Firebase service account key JSON file
    FIREBASE_CREDENTIALS = os.environ.get('FIREBASE_CREDENTIALS', './resq-database-firebase-adminsdk-fbsvc-e056194891.json')
    # Your Firebase Realtime Database URL
    FIREBASE_DATABASE_URL = os.environ.get('FIREBASE_DATABASE_URL', 'https://resq-database-default-rtdb.firebaseio.com/')
