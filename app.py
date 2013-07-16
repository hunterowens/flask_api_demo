from flask import Flask,jsonify
import json
app = Flask(__name__)

@app.route('/user')
def user():
	return json.dumps({"id":5,"name":"hunter"})

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()