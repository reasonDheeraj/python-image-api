from flask import Flask,json,request, Response,jsonify,make_response
import os
import numpy as numpy
import cv2
import io

app = Flask(__name__)

@app.route('/helloWorld')
def helloWorld():
    return "Hello World"

def detect_text(imageName):
    from google.cloud import vision
    from google.cloud.vision import types
    client = vision.ImageAnnotatorClient()
    file_name = os.path.abspath(imageName)
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    responseData = []
    for text in texts:
        responseData.append(text.description)
    print(responseData)
    return responseData

@app.route('/get_text', methods = ['POST'])
def upload_file():
    req = request.get_json()
    file = request.files['file']
    file.save("image.jpg")
    data = detect_text("image.jpg")
    res = make_response(jsonify({"Success" : data}), 200)
    return res

if __name__ == "__main__":
    app.run()		# For local machine app.run(host='0.0.0.0')
