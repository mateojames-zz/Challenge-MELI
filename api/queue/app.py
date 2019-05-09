#!/usr/local/bin/python3

import redis
from flask import Flask, request, json, Response, render_template

app = Flask(__name__)
client = redis.Redis(host = '192.168.99.100', port = 6379, db=0, charset="utf-8", decode_responses=True)

@app.route('/')
def index():
    lista=client.lrange('queue', 0, -1)
    return render_template("index.html", lista=lista)

@app.route('/restore')
def restore():
    n=client.llen('queue')
    if n!=0:
        for i in range(n):
            client.blpop('queue')

    client.lpush('queue','Locura','Cerveza','Uno')
    lista=client.lrange('queue', 0, -1)
    return render_template("index.html", lista=lista)

@app.route('/pop/<msg>', methods=["POST"])
def popQueue(msg):
    if request.headers['Content-Type'] == 'application/json':
        client.blpop('queue')

        data = {
            'status'  : 'ok',
            'message' : msg
        }
        js = json.dumps(data)

        resp = Response(js, status=200, mimetype='application/json')
    else:
        data = {
            'status'  : 'super not ok',
            'message' : 'Content type was not JSON'
        }
        js = json.dumps(data)

        resp = Response(js, status=401, mimetype='application/json')

    return resp


@app.route('/push', methods=["POST"])
def pushQueue():
    if request.headers['Content-Type'] == 'application/json':
        content = request.get_json()
        value = content['msg']
        client.lpush('queue', value)
        
        data = {
            'status'  : 'ok'
        }
        js = json.dumps(data)

        resp = Response(js, status=200, mimetype='application/json')
    else:
        data = {
            'status'  : 'super not ok',
            'message' : 'Content type was not JSON'
        }
        js = json.dumps(data)
        resp = Response(js, status=401, mimetype='application/json')
    return resp
    
  
@app.route('/count', methods=["GET"])
def countQueue():
    count=client.llen('queue')
    data = {
        'status'  : 'ok',
        'count' : count
    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp

 
if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)