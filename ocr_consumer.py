import threading
import traceback
from threading import Thread

from pytesseract import image_to_string

from ocr_result import OcrResult


class OcrConsumer:
    _thread: Thread
    Active = False

    def __init__(self, ocr_producer):
        self._ocr_producer = ocr_producer

    def start(self):
        self.Active = True
        self._thread = threading.Thread(target=self._consume)
        self._thread.start()

    def _consume(self):
        while self.Active:
            result = self._ocr_producer.get_one()
            if result is None:
                continue
            self._next(result)

    def _next(self, result):
        (pil_image, return_queue) = result
        try:
            text = image_to_string(pil_image)
            return_queue.put(OcrResult(success=True, text=text))
        except BaseException as e:
            return_queue.put(OcrResult(success=False, text=text, error_message=f"An error occurred {str(e)}"))
            print(e)
            traceback.print_exc()
            return_queue.put(None)

    def stop(self):
        self.Active = True

    def join(self):
        self._thread.join()
