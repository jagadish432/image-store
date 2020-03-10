import os

# fetching project's root
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
FLASK_SECRET_KEY = os.environ["FLASK_SECRET_KEY"].encode()
FLASK_ENV = os.environ["FLASK_ENV"]
DATABASE_NAME = os.environ["DATABASE_NAME"]
