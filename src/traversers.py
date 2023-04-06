'''
This module contains classes used to represent the hierarchical
structure of a Symphony's code.
'''

class Node:
    '''
    Base class for reprsenting logic nodes in a Symphony's code.
    '''
    def __init__(self, parent=None) -> None:
        if parent is not None and not isinstance(parent, Node):
            raise ValueError(f'''
                Parmeter {parent} was of type {type(parent)}
                Constructor method expected this paremter to be a
                Node or a NoneType object.
            ''')
        self.parent = parent
