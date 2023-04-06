'''
This module contains classes related to input
and output files.
'''

class File:
    '''
    Base class used for interacting with files
    of variosu type.
    '''
    def __init__(self, fname: str) -> None:
        self.fname = fname
        with open(fname) as f:
            self.contents = f.read().strip()
            f.close()


class InputFile(File):
    '''
    Input files contain the Symphony code that will
    be parsed and analyzed by the program.
    '''
    def __init__(self, fname: str) -> None:
        super().__init__(fname)


class OutputFile(File):
    '''
    Output files are the destination of data or parsed
    code.
    '''
    def __init__(self, fname: str) -> None:
        self.fname = fname


