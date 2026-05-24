import os
import json
import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore


firebase_json = json.loads(
    os.getenv("FIREBASE_CREDENTIALS_JSON")
)

cred = credentials.Certificate(firebase_json)

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()

def save_report_metadata(data):

    print("🔥 SAVING TO FIRESTORE")
    print(data)

    result = db.collection("reports").add(data)

    print("✅ FIRESTORE SAVE OK")
    print(result)
