from typing import List, Pattern


class OcrMatcher:
    regex_list: List[Pattern[str]]
    event_name: str

    def __init__(self, event_name: str, regex_list: List[Pattern[str]] ):
        self.event_name = event_name
        self.regex_list = regex_list

    def match_text(self, text):
        for a in self.regex_list:
            if a.search(text):
                return self.event_name
        return None
