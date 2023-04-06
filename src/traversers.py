'''
This module contains classes used to represent the hierarchical
structure of a Symphony's code.
'''

from .base import BaseNode

class ConditionalNode(BaseNode):
    def __init__(self, parent=None|BaseNode) -> None:
        super().__init__(parent)

class FilterNode(BaseNode):
    def __init__(self, parent=None|BaseNode) -> None:
        super().__init__(parent)

class AssetNode(BaseNode):
    def __init__(self, parent=None|BaseNode) -> None:
        super().__init__(parent)

class WeightNode(BaseNode):
    def __init__(self, parent=None|BaseNode) -> None:
        super().__init__(parent)