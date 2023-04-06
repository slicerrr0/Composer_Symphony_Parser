'''
This module contains classes used to represent the hierarchical
structure of a Symphony's code.
'''

from .base import BaseNode, BaseGroup


### Node classes
class ConditionalNode(BaseNode):
    '''
    Conditional nodes function as switches between multiple
    logic paths, the path that the algorithm takes being
    dependent on the boolean evaluation of the expression 
    associated with the conditional node.
    '''
    def __init__(self, parent=None|BaseNode) -> None:
        super(ConditionalNode, self).__init__(parent)

class FilterNode(BaseNode):
    '''
    Filter nodes sort 
    '''
    def __init__(self, indicator: str, amount: int, reverse=False, parent=None|BaseNode) -> None:
        super(FilterNode, self).__init__(parent)
        self.indicator = indicator
        self.amount = amount
        self.reverse = reverse

class AssetNode(BaseNode):
    def __init__(self, assets: list[str], parent=None|BaseNode) -> None:
        super(AssetNode, self).__init__(parent)
        self.assets = assets

class WeightNode(BaseNode):
    def __init__(self, weight: float, parent=None|BaseNode) -> None:
        super(WeightNode, self).__init__(parent)
        self.weight = weight


### Group classes
class Group(BaseGroup):
    def __init__(self, name: str) -> None:
        super(BaseGroup, self).__init__(name)