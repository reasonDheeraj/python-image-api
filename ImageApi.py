from flask import Flask, Response
import os
import numpy as numpy
import cv2

app = Flask(__name__)

@app.route('/helloWorld')
def helloWorld():
	return "Hello World"

if __name__ == "__main__":
    app.run()		# For local machine app.run(host='0.0.0.0')
