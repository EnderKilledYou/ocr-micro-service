import threading
import traceback
from threading import Thread

from pytesseract import image_to_string

from ocr_matcher import OcrMatcher
from ocr_result import OcrResult


class OcrConsumer:
    _thread: Thread
    Active = False
    matcher_list = [OcrMatcher]

    def __init__(self, ocr_producer, matcher_list):
        self._ocr_producer = ocr_producer
        self.matcher_list = matcher_list

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

    def _match(self, text: str):
        matches = []
        for matcher in self.matcher_list:
            match_text = matcher.match_text(text)
            if match_text is not None:
                matches.append(match_text)
        return matches

    def _next(self, result):
        (pil_image, return_queue) = result
        try:
            text = image_to_string(pil_image)
            return_queue.put(OcrResult(success=True, text=text, matches=self._match(text)))
        except BaseException as e:
            return_queue.put(OcrResult(success=False, text=text, error_message=f"An error occurred {str(e)}"))
            print(e)
            traceback.print_exc()

    def stop(self):
        self.Active = True

    def join(self):
        self._thread.join()
