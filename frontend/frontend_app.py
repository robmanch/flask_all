from flask import Flask, render_template, request, redirect, url_for
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    if not num1 or not num2:
        print("Missing input values")
        return redirect(url_for('index'))

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Invalid input values")
        return "Invalid input. Please enter numeric values.", 400

    try:
        cert_path = r"D:\deploy_test\flask_all\frontend\flask.crt"
        response = requests.post('https://127.0.0.1:5000/add', json={'num1': num1, 'num2': num2}, verify=cert_path)
        response.raise_for_status()
        result = response.json().get('result')
    except requests.RequestException as e:
        print(f"Error while calling the backend API: {e}")
        return "An error occurred while trying to calculate the result.", 500

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
