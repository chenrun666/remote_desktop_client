import os

BASEDIR = os.path.dirname(os.path.dirname(__file__))

USER = "root"
EMAIL = "984598654@qq.com"

MODE = "AGENT"
DEBUG = True

API = "http://127.0.0.1:8000/api/asset/"

CERT_PATH = os.path.join(BASEDIR, "config/cert")

PLUGINS_DICT = {
    'basic': 'src.plugins.basic.Basic',
}
