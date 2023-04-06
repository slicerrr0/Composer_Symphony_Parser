'''
This module contains the base implementations of class
types used throughout the program.
'''


class BaseFile:
    '''
    Base class used for interacting with files
    of various type.
    '''
    def __init__(self, fname: str) -> None:
        self.fname = fname
        with open(fname) as f:
            self.contents = f.read().strip()
            f.close()


class BaseNode:
    '''
    Base class for reprsenting logic nodes in a Symphony's code.
    '''
    def __init__(self, parent=None) -> None:
        if parent is not None and not isinstance(parent, BaseNode):
            raise ValueError(f'''
                Parmeter {parent} was of type {type(parent)}
                Constructor method expected this paremter to be a
                Node or a NoneType object.
            ''')
        self.parent = parent

class BaseParser:
    '''
    Base parser class. 
    '''
    def __init__(self, text: str) -> None:
        self.text = text
