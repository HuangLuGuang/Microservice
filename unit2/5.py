# -*- coding: utf-8 -*-
# @createTime    : 2019/7/17 23:05
# @author  : Huanglg
# @fileName: 3.py
# @email: luguang.huang@mabotech.com
from flask import Flask, jsonify, g, request, request_finished
from flask.signals import signals_available

if not signals_available:
    raise RuntimeError("pip install blinker")


app = Flask(__name__)

def finished(sender, response, **extra):
    print("about to send response")
    print(response.get_data())

request_finished.connect(finished)

@app.route('/api')
def my_microservice():
    return jsonify({'hello': "world"})

if __name__ == '__main__':
    app.run()
