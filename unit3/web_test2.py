# -*- coding: utf-8 -*-
# @createTime    : 2019/7/21 20:32
# @author  : Huanglg
# @fileName: web_test1.py
# @email: luguang.huang@mabotech.com
import unittest
import os

os.environ.setdefault('HTTP_SERVER', 'http://127.0.0.1:5000/')


class TestMyApp(unittest.TestCase):

    def setUp(self):
        http_server = os.environ.get('HTTP_SERVER')
        if http_server is not None:
            from webtest import TestApp
            self.app = TestApp(http_server)
        else:
            from unit2.api_test import app as testapp
            from flask_webtest import TestApp
            self.app = TestApp(testapp)

    def test_help(self):
        hello = self.app.get('/api')
        self.assertEqual(hello.json['Hello'], "World")



if __name__ == '__main__':
    unittest.main()
