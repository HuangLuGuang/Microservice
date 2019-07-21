# -*- coding: utf-8 -*-
# @createTime    : 2019/7/17 22:13
# @author  : Huanglg
# @fileName: 1.py
# @email: luguang.huang@mabotech.com
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api')
def my_microservice():
    print(request)
    print(request.environ)
    response = jsonify({'Hello': "World"})
    print(response)
    print(response.data)
    return response

@app.route('/api/person/<person_id>')
def person(person_id):
    response = jsonify({'Hello': person_id})
    return response

if __name__ == '__main__':
    print(app.url_map)
    app.testing = True
    app.run(debug = True)
