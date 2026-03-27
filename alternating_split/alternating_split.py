"""
Docstring for alternating_split.alternating_split
"""

class Node:

    """
    Docstring for Node
    """

    def __init__(self, data = None):
        self.data = data
        self.next = None

class Context(object):

    """
    Docstring for Context
    """

    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head: Node):

    """
    Docstring for alternating_split
    """

    # Your code goes here.
    # Remember to return the context.

    if head is None or head.next is None:
        raise ValueError("Cannot split an empty list")

    d1 = Node(None)
    d2 = Node(None)

    t1 = d1
    t2 = d2

    current = head
    first = True

    while current is not None:
        if first:
            t1.next = current
            t1 = t1.next # move the tail pointer forward

        else:
            t2.next = current
            t2 = t2.next # move the tail pointer forward

        # flip and move
        current = current.next
        first = not first

    # linking
    t1.next = None
    t2.next = None

    return Context(d1.next, d2.next)
