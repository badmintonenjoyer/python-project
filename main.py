import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from CI/CD deployed app!"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8181))
    app.run(host="0.0.0.0", port=port)
