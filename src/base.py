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


class BaseSymphony:
    '''
    Base class for representing Symphony algorithms.
    '''
    def __init__(self, name: str, rebalance=None) -> None:
        self.name = name
        if rebalance is not None and type(rebalance) != float:
            raise ValueError(f'''
                Parameter {rebalance} was of type {str(type(rebalance))}.
                This parameter must be a float or a NoneType object.
            ''')
        self.rebalance = rebalance

class BaseNode:
    '''
    Base class for representing logic nodes in a Symphony's code.
    '''
    def __init__(self, parent=None) -> None:
        if parent is not None and not isinstance(parent, BaseNode):
            raise ValueError(f'''
                Parmeter {parent} was of type {str(type(parent))}
                Constructor method expected this paremter to be a
                Node or a NoneType object.
            ''')
        self.parent = parent


class BaseGroup:
    '''
    Base class representing "groups" within a Symphony's code.
    "Groups" are titled portions of a Symphony containing descendent
    Nodes.
    '''
    def __init__(self, name: str) -> None:
        self.name = name

class BaseParser:
    '''
    Base parser class. 
    '''
    def __init__(self, text: str) -> None:
        self.text = text
    
