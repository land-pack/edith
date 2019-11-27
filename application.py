from flask import Flask

application = Flask(__name__)
#application.config['SERVER_NAME']= '0.0.0.0:8080'

print("landpack-")

@application.route("/")
def index():
    return "Hello Edith"

