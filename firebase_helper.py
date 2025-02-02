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
    Returns a reference to the 'resq-database' node in the Firebase Realtime Database.
    """
    return db.reference('resq-database')


def insert_processed_json(processed_json):
    """
    Inserts the processed JSON into the 'resq-database' node
    in your Firebase Realtime Database and returns the generated key.
    """
    # Get a reference to the resq-database node
    ref = db.reference('resq-database')
    
    # Push the processed JSON into the database
    new_response_ref = ref.push(processed_json)
    
    # Return the unique key generated for this new record
    return new_response_ref.key


def update_processed_json(response_id, processed_json):
    """
    Updates the existing emergency response with the provided data.
    """
    # Get a reference to the resq-database node
    ref = db.reference('resq-database')
    
    # Update the existing emergency response with the provided data
    ref.child(response_id).update(processed_json)
    
    return response_id