'''
This module contains classes related to input
and output files.
'''

from .base import BaseFile

class InputFile(BaseFile):
    '''
    Input files contain the Symphony code that will
    be parsed and analyzed by the program.
    '''
    def __init__(self, fname: str) -> None:
        super(InputFile, self).__init__(fname)


class OutputFile(BaseFile):
    '''
    Output files are the destination of data or parsed
    code.
    '''
    def __init__(self, fname: str) -> None:
        self.fname = fname


