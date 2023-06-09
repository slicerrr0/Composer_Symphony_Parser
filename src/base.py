'''
This module contains the base implementations of class
types used throughout the program.
'''

import re
from .traversers import ConditionalNode, WeightNode

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
        # Regular expression patterns
        self.REBALANCE_PATTERN = r'(?<={:rebalance-threshold )[^}]+'
        
        self.BASE_NODE_PATTERN = ''
        self.CONDITIONAL_NODE_PATTERN_VARIABLE = ''
        self.CONDITIONAL_NODE_PATTERN_CONSTANT = ''
        self.FILTER_NODE_PATTERN = ''
        self.ASSET_NODE_PATTERN = ''
        self.WEIGHT_NODE_PATTERN = ''
    def parse_rebalance_threshold(self) -> float:
        '''
        Parses `self.text` for a match to `self.REBALANCE_PATTERN`. This 
        match corresponds to the rebalance threshold set for the Symphony.
        '''
        return float(re.search(self.REBALANCE_PATTERN, self.text).group(0))
    def parse_weight_node(self) -> WeightNode:
        return
    def parse_conditional_node(self, node: str) -> ConditionalNode:
        return
    def parse_all_nodes(self) -> list[str]:
        '''
        Parses `self.text` for all distinct logic Nodes
        within the Symphony using the regex pattern specified
        in `self.NODE_PATTERN`.
        '''
        return re.findall(self.NODE_PATTERN, self.text)