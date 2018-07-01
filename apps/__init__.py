from flask import Flask
from apps.database import init_db

app = Flask(__name__)
init_db(app)

import apps.views
