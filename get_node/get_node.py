"""
Docstring for CodewarsLinkedList.get_node.get_node
"""

class Node:

    """
    Docstring for Node
    """

    def __init__(self, data, n = None):
        self.data = data
        self.next = n


def get_nth(node: Node, index: int):

    """
    Docstring for get_nth
    """

    if not isinstance(index, int) or index < 0:
        raise ValueError("Index must be a non-negative integer")

    current = node
    i = 0

    while current is not None and i < index:
        current = current.next
        i += 1

    if current is None:
        raise ValueError("Index out of bounds or empty list")

    return current
