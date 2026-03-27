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

def remove_duplicates(head: Node):

    """
    Docstring for sorted_insert
    """

    # Your code goes here.
    # Make sure to return the head of the list.

    current = head
    while current is not None and current.next is not None:
        if current.data == current.next.data:
            # skip the duplicate node
            current.next = current.next.next
        else:
            # move forward if no duplicate was found
            current = current.next

    return head
