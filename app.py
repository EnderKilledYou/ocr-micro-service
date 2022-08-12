from PIL import Image
from flask import Flask, jsonify, request

from ocr_producer import OcrProducer

app = Flask(__name__)

job_queue = OcrProducer()
job_queue.start()


@app.route('/ocr', methods=['POST'])
def ocr():  # put application's code here
    img = Image.open(fp=request.files['image'].stream)
    return job_queue.wait_text(img, 15).to_dict()


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5008)
