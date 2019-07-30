from flask import Flask
app = Flask(__name__)
from Routes import productRoute
from db import db

