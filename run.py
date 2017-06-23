from app import app
from app import views
from flask import session
import os

from flask import Session
app.secret_key = 'super secret key'
if __name__ == '__main__':
    sess = Session()

    app.config['SESSION_TYPE'] = 'filesystem'

    app.debug = True
    app.run()
