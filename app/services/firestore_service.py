import os
import json
import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore


firebase_json = json.loads(
    os.getenv("FIREBASE_CREDENTIALS_JSON")
)

cred = credentials.Certificate(firebase_json)

firebase_admin.initialize_app(cred)

db = firestore.client()

def save_report_metadata(data):

    db.collection("reports").add(data)

    