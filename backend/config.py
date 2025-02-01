import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my_secret_key')
    # Path to your Firebase service account key JSON file
    FIREBASE_CREDENTIALS = os.environ.get('FIREBASE_CREDENTIALS', 'path/to/serviceAccountKey.json')
    # Your Firebase Realtime Database URL
    FIREBASE_DATABASE_URL = os.environ.get('FIREBASE_DATABASE_URL', 'https://resq-database-default-rtdb.firebaseio.com/')
