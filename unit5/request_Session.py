# -*- coding: utf-8 -*-
# @createTime    : 2019/7/31 22:18
# @author  : Huanglg
# @fileName: 1.py
# @email: luguang.huang@mabotech.com
from requests import Session

def setup_connector(app, name='default', **options):

    if not hasattr(app, 'extensions'):
        app.extensions = {}

    if 'connectors' not in app.extensions:
        app.extensions['connectors'] = {}
    session = Session()

    if 'auth' in options:
        session.auth = options['auth']
    hearders = options.get('hearders', {})

    if 'Content-Type' not in hearders:
        hearders['Content-Type'] = 'appli cation/json'
    session.headers.update(hearders)

    app.extensions['connectors'][name] = session
    return session

def get_connector(app, name='default'):
    return app.extensions['connectors'][name]
