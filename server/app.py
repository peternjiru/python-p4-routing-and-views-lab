#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param


@app.route('/count/<int:param>')
def count(param):
    my_range = range(param)
    output = ""
    for x in my_range:
        output += f"{x}\n"
    return output


@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    elif operation == "*":
        answer = num1 * num2
    elif operation == "div":
        answer = num1 / num2
    elif operation == "%":
        answer = num1 % num2
    return str(answer)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
