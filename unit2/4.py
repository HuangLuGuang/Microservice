# -*- coding: utf-8 -*-
# @createTime    : 2019/7/17 23:05
# @author  : Huanglg
# @fileName: 3.py
# @email: luguang.huang@mabotech.com
from flask import Flask, jsonify, g, request

app = Flask(__name__)

@app.before_request
def authenticate():
    if request.authorization:
        g.user = request.authorization['username']
    else:
        g.user = 'Anonymous'

@app.route('/api')
def my_microservice():
    return jsonify({'hello': g.user})

if __name__ == '__main__':
    app.run()
