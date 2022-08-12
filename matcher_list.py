import re

from ocr_matcher import OcrMatcher

overwatch_matcher_list:[OcrMatcher] = [
    OcrMatcher('elim', [re.compile('[MI]{1,2}NATE[ED]{1,2}', re.IGNORECASE)]),
    OcrMatcher('healing', [re.compile('HEALING', re.IGNORECASE)]),
    OcrMatcher('hero_select', [re.compile('PRESS H TO CHANGE HERO', re.IGNORECASE)]),
    OcrMatcher('defense', [re.compile('DEFENSE', re.IGNORECASE)]),
    OcrMatcher('orbed', [re.compile('GAINED', re.IGNORECASE)]),
    OcrMatcher('slept', [re.compile('SLEPT', re.IGNORECASE)]),
    OcrMatcher('block', [re.compile('BLOCKING', re.IGNORECASE)]),
    OcrMatcher('death', [re.compile('(NATED BY|YOU WERE)', re.IGNORECASE)]),
    OcrMatcher('assist', [re.compile('ASSIST', re.IGNORECASE)]),
]


testing_matcher_list = [
OcrMatcher('google', [re.compile('google', re.IGNORECASE)])
]