from app import app
from config import config


if __name__ == '__main__':
    app.run(config.HOST, config.PORT)
