# -*- coding: utf-8 -*-
# @createTime    : 2019/7/20 23:36
# @author  : Huanglg
# @fileName: funcTest.py
# @email: luguang.huang@mabotech.com
import json
import unittest

from flask import Flask
from flask_basic import app as tested_app

class TestApp(unittest.TestCase):

    def test_help(self):
        # app = Flask(__name__)
        from unit2.api_test import app
        client = app.test_client()
        hello = client.get('/api')
        body = json.loads(str(hello.data, 'utf-8'))
        self.assertEqual(body['Hello'], "World")

