from flask_restful import Api
from flask import Flask, request
from codetutor.ext.db import url, db
from flask_cors import CORS
from codetutor.ext.routes import initialize_routes
import json

app = Flask(__name__)
CORS(app, resources={r'/api/*': {"origins": "*"}})
print(url)
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
db.init_app(app)
api = Api(app)

with app.app_context():
    db.create_all()
initialize_routes(api)
