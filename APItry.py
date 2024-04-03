# api.py
import os
from flask import Flask, request, jsonify
from google.cloud import vision

# Set your Google Cloud credentials environment variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:\python_1\pythonProject\glassy-vial-413609-104ff6f112ad.json"

app = Flask(__name__)


@app.route('/extract_text', methods=['POST'])
def extract_text():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image_file = request.files['image']
    image_content = image_file.read()

    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=image_content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if texts:
        extracted_text = texts[0].description
        return jsonify({'text': extracted_text}), 200
    else:
        return jsonify({'text': 'No text found in the image.'}), 404


if __name__ == '__main__':
    app.run(debug=True)
