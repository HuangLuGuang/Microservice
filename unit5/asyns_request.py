# -*- coding: utf-8 -*-
# @createTime    : 2019/7/31 22:31
# @author  : Huanglg
# @fileName: asyns_request.py
# @email: luguang.huang@mabotech.com
import sys

from requests.exceptions import ReadTimeout, ConnectionError

sys.path.append('F:\\code\\Microservice')
from flask import Flask, jsonify

from unit5.request_Session import setup_connector, get_connector


app = Flask(__name__)
setup_connector(app)


@app.route('/api', methods=['GET', 'POST'])
def my_microservice():

    with get_connector(app) as conn:
        try:
            result = conn.get('http://localhost:5000/api', timeout=2).json()
        except (ConnectionError, ReadTimeout):
            result = {}
    return jsonify({'result': result, 'Hello': 'World'})


if __name__ == '__main__':
    app.run(port=5001, debug=True)
