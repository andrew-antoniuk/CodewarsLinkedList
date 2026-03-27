"""
Docstring for recursive_reverse.recurive_reverse
"""

class Node:

    """
    Docstring for Node
    """

    def __init__(self, data = None):
        self.data = data
        self.next = None

def reverse(head: Node):

    """
    Docstring for reverse

    :param head: Description
    """

    # your code goes here

    # if cur is None:
    #     cur = head
    #     n = cur.next

    if head is None or head.next is None:
        return head

    # reverse the rest of the list
    new = reverse(head.next)

    head.next.next = head  # make the next node point back
    head.next = None       # break the original link

    return new
