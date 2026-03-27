"""
Docstring for CodewarsLinkedList.move_node.move_node
"""

class Node:

    """
    Docstring for Node
    """

    def __init__(self, data, n = None):
        self.data = data
        self.next = n


class Context(object):

    """
    Docstring for Context

    """
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source: Node, dest):

    """
    Docstring for move_node
    """

    # Your code goes here.
    # Remember to return the context.

    if source is None:
        raise ValueError("Cannot move node from an empty source list.")

    node = source
    source = source.next

    node.next = dest
    dest = node

    return Context(source, dest)
