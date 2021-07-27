from flask import Flask
from config import config
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(config)
CORS(app)


from app import routes
