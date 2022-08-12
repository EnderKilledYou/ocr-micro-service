import traceback
from queue import Queue, Empty

from ocr_consumer import OcrConsumer
from ocr_matcher import OcrMatcher
from ocr_result import OcrResult


class OcrProducer:
    time_out: int
    consumers = []

    def __init__(self, matcher_list: [OcrMatcher], thread_count=20, time_out: int = 15):

        self.time_out = time_out
        self.consumers = []
        self.queue = Queue()
        for i in range(0, thread_count):
            consumer = OcrConsumer(self, matcher_list)
            self.consumers.append(consumer)



    def start(self):
        for c in self.consumers:
            c.start()

    def stop(self):
        print("exiting")
        for c in self.consumers:
            c.stop()

    def put(self, item):
        self.queue.put(item)

    def get_one(self):
        try:
            return self.queue.get(True, self.time_out)
        except Empty as p:
            pass
        except BaseException as e:
            print(e)
            traceback.print_exc()
            return None

    def wait_text(self, img, time_out) -> OcrResult:
        return_queue = Queue()
        self.queue.put((img, return_queue))
        try:
            return return_queue.get(True, time_out)
        except Empty as e:
            return OcrResult(success=False, error_message="ocr time out")
