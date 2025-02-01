import firebase_admin
from firebase_admin import credentials, db
from config import Config

# Initialize Firebase app only once
if not firebase_admin._apps:
    cred = credentials.Certificate(Config.FIREBASE_CREDENTIALS)
    firebase_admin.initialize_app(cred, {
        'databaseURL': Config.FIREBASE_DATABASE_URL
    })

def get_db():
    """
    Returns a reference to the 'emergency_responses' node in the Firebase Realtime Database.
    """
    return db.reference('emergency_responses')
