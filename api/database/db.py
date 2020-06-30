from flask_mongoengine import MongoEngine
from flask import Flask


db = MongoEngine()

def initialize_app(app: Flask):
  from config import Config
  data_config = Config().data['MONGO']

  app.config['MONGODB_SETTINGS'] = {
    'host': data_config['URI']
  }

  db.init_app(app)
