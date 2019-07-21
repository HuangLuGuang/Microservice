# -*- coding: utf-8 -*-
# @createTime    : 2019/7/21 20:32
# @author  : Huanglg
# @fileName: web_test1.py
# @email: luguang.huang@mabotech.com
import unittest
from flask_webtest import TestApp


class TestMyApp(unittest.TestCase):

    def test_help(self):
        from unit2.api_test import app as testapp
        app = TestApp(testapp)
        hello = app.get('/api')
        self.assertEqual(hello.json['Hello'], "World")


if __name__ == '__main__':
    unittest.main()
