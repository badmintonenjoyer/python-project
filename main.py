from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form.get('num1', 0))
        num2 = float(request.form.get('num2', 0))
        result = num1 + num2
        return render_template('index.html', result=result, num1=num1, num2=num2)
    except ValueError:
        return render_template('index.html', error="Proszę wpisać poprawne liczby.")

@app.route('/health')
def health():
    # Możesz tutaj dodać więcej sprawdzeń (np. DB, serwisy)
    return jsonify(status="OK", service="Python Flask app", version="1.0")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
