# Initialization file

from flask import Flask

# initialize the bucketlist application
app = Flask(__name__, instance_relative_config=True)

# load the views
from app import views

app.config.from_object('config')
