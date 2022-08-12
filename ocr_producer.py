from queue import Queue, Empty

from ocr_consumer import OcrConsumer
from ocr_result import OcrResult


class OcrProducer:
    time_out: int
    consumers = []

    def __init__(self, thread_count=20, time_out: int = 15):
        self.time_out = time_out
        self.consumers = []
        for i in range(0, thread_count):
            self.consumers.append(OcrConsumer(self))

    queue = Queue()

    def start(self):
        for c in self.consumers:
            c.start()

    def stop(self):
        for c in self.consumers:
            c.stop()
        for c in self.consumers:
            c.join()

    def put(self, item):
        self.queue.put(item)

    def get_one(self):
        try:
            return self.queue.get(True, self.time_out)
        except:
            return None

    def wait_text(self, img, time_out) -> OcrResult:
        return_queue = Queue()
        self.queue.put((img, return_queue))
        try:
            return return_queue.get(True, time_out)
        except Empty as e:
            return OcrResult(success=False, error_message="ocr time out")
