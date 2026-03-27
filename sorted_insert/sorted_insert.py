"""
Docstring for sorted_insert.sorted_insert
"""

class Node:

    """
    Docstring for Node
    """

    def __init__(self, data, n = None):
        self.data = data
        self.next = n


def sorted_insert(head: Node, data):

    """
    Docstring for sorted_insert
    """

    # Your code goes here.
    # Make sure to return the head of the list.

    prev = Node(data)
    if head is None or head.data >= data:
        prev.next = head
        return prev

    current = head
    while current.next is not None and current.next.data < data:
        current = current.next

    prev.next = current.next
    current.next = prev

    return head
