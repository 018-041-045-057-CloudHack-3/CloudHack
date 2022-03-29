from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'

""""
old monolithic arch code 
def add(n1, n2):
    return n1+n2

def minus(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2
"""


@app.route('/', methods=['POST', 'GET'])
def index():

    number_1 = request.form.get("first")
    
    if number_1 is None:
    	number_1 = '0'
    	
    number_2 = request.form.get('second')
    
    if number_2 is None:
    	number_2 = '0'
    	
    number_1 = int(number_1)
    number_2 = int(number_2)
    
    operation = request.form.get('operation')
    result = 0
   	
    
    
    if operation == 'add':
        result = requests.get(url = f'http://add-service:5051/{number_1}/{number_2}').text
    elif operation == 'minus':
        result = requests.get(url = f'http://minus-service:5052/{number_1}/{number_2}').text
    elif operation == 'multiply':
        result = requests.get(url = f'http://multiply-service:5053/{number_1}/{number_2}').text
    elif operation == 'divide':
        result = requests.get(url = f'http://divide-service:5054/{number_1}/{number_2}').text
    elif operation == 'gcd':
        result = requests.get(url = f'http://gcd-service:5055/{number_1}/{number_2}').text
    elif operation == 'lcm':
        result = requests.get(url = f'http://lcm-service:5056/{number_1}/{number_2}').text
    elif operation == 'modulus':
        result = requests.get(url = f'http://modulus-service:5057/{number_1}/{number_2}').text

    
    flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
