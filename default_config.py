import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class DevConfiguration:
    DEBUG = True
    HOST = '127.0.0.1'
    PORT = 5557
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'

    IMAGES_FOLDER = ""


config = DevConfiguration()
