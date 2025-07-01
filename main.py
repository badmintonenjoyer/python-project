from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health')
def health():
    return (
        "Status aplikacji: OK\n"
        "Usługa: Python Flask app\n"
        "Wersja: 1.0\n"
    ), 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)