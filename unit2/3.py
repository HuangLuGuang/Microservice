# -*- coding: utf-8 -*-
# @createTime    : 2019/7/17 23:05
# @author  : Huanglg
# @fileName: 3.py
# @email: luguang.huang@mabotech.com
from flask import Flask, g
import yaml

def yamlify(data, status=200, headers=None):
    _headers = {"Content-Type": "application/x-yaml"}
    if headers is not None:
        _headers.update(headers)
    return yaml.safe_dump(data), status, _headers

app = Flask(__name__)

@app.route('/api')
def my_microservice():
    return yamlify(['hello', 'yaml', 'world!'])
if __name__ == '__main__':
    app.run()
