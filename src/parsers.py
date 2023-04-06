'''
This module contains classes used to digest Symphony code and
transform it into python objects.
'''

from .base import BaseParser

class Parser(BaseParser):
    def __init__(self, text: str) -> None:
        super(Parser, self).__init__(text)

