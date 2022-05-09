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
    try:
        id=request.json['id']
        todos.document(id).set(request.json)
        return jsonify({"sucess":True}),200
    except Exception as e:
        return f"An error occured {e}"

@app.route('/list',methods=['GET'])
def read():
    try:
        todo_id=request.args.get('id')
        if todo_id:
            todo=todos.document(todo_id).get();
            return jsonify(todo.to_dict()),200
        else:
            all_todos=[doc.to_dict() for doc in todos.stream()]
            return jsonify(all_todos),200
    except Exception as e:
        return f"An error occured {e}"

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)
