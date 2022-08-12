from typing import List
from waitress import serve
from PIL import Image
from flask import Flask, jsonify, request
from matcher_list import overwatch_matcher_list, testing_matcher_list
from ocr_producer import OcrProducer


app = Flask(__name__)

job_queue = OcrProducer(overwatch_matcher_list)
job_queue.start()

test_job_queue = OcrProducer(testing_matcher_list, thread_count=1)
test_job_queue.start()

job_queues: List[OcrProducer] = [job_queue, test_job_queue]


@app.route('/ocr', methods=['POST'])
def ocr():
    img = Image.open(fp=request.files['image'].stream)
    if 'testing' in request.args:
        return test_job_queue.wait_text(img, 15).to_dict()
    return job_queue.wait_text(img, 15).to_dict()


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5008)
