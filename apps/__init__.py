from flask import Flask
from apps.database import init_db

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' # todo
app.config.from_object('apps.config.Config')
init_db(app)

import apps.views
