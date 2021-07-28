from flask import Flask
from config import config
from flask_cors import CORS
from app.routes import bp

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(bp)
CORS(app)


@app.context_processor
def inject_url_prefix():
    return dict(url_prefix=config.URL_PREFIX)

