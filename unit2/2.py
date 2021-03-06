# -*- coding: utf-8 -*-
# @createTime    : 2019/7/17 22:36
# @author  : Huanglg
# @fileName: 2.py
# @email: luguang.huang@mabotech.com
from flask import Flask, jsonify, request, Response
from werkzeug.routing import BaseConverter, ValidationError

_USERS = {"1": "Tarek", '2': 'Freya'}
_IDS = {val:id for id, val in _USERS.items()}

class RegisteredUser(BaseConverter):
    def to_python(self, value):
        if value in _USERS:
            return _USERS[value]
        raise ValidationError

    def to_url(self, value):
        return _IDS[value]

app = Flask(__name__)

app.url_map.converters['registered'] = RegisteredUser

@app.route('/api/person/<registered:name>')
def person(name):
    response = jsonify({"hello hey": name })
    return response


if __name__ == '__main__':
    app.run(debug = True)
