import sys
sys._stdout = sys.stdout
sys.stdout = sys.stderr

from flask import Flask
from flask.ext.mongoengine import MongoEngine
import logging
import json

settings = json.loads(open("config/config.json").read())

app = Flask(__name__)
app.template_folder = "templates"
app.config["MONGODB_SETTINGS"] = {'DB': "destrock"}
app.config["SECRET_KEY"] = settings.get("secret_key", "SuPeRsECrEt")
db = MongoEngine(app)
application = app


def register_blueprints(app):
    from blog.views import posts
    from blog.admin import admin
    app.register_blueprint(posts)
    app.register_blueprint(admin)

register_blueprints(app)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    app.run(host="0.0.0.0", port=5000, use_reloader=True)
