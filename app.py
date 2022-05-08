import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

app=Flask(__name__)

cred=credentials.Certificate('ptflaskwithfirebase-firebase-adminsdk.json')
default_app=initialize_app(cred)
db=firestore.client()
todos=db.collection('todos')

@app.route('/add',methods=['POST'])
def create():
    