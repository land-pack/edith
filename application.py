from flask import Flask

app = Flask(__name__)

print("landpack-")

@app.route("/")
def index():
    return "Hello Edith"

if __name__ == '__main__':
    print("landpack-listen")
    app.run(host="0.0.0.0", port=8080)
