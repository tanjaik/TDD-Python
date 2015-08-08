from flask import Flask 
from test_fizzbuzz import FizzBuzz

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello World"

@app.route('/fizzbuzz/<number>')
def fizzbuzz(number):
	fizzbuzz = FizzBuzz()
	return fizzbuzz.count(number)


if __name__ == '__main__':
	app.run()