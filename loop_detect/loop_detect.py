"""
Docstring for loop_detect.loop_detect
"""

class Node:

    """
    Docstring for Node
    """

    def __init__(self, data, n = None):
        self.data = data
        self.next = n


def detect(head: Node):

    """
    Docstring for detect
    """

    if head is None or head.next is None:
        return False

    slow = head
    fast = head

    while fast is not None and fast.next is not None:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def loop_size(head: Node):

    """
    Docstring for loop_size
    """

    if head is None or head.next is None:
        return 0

    slow = head
    fast = head

    while fast is not None and fast.next is not None: # cycling

        slow = slow.next
        fast = fast.next.next

        if slow == fast: # loop detect

            count = 1
            fast = fast.next

            while slow != fast: # slower
                # iterate until slow is reached again
                fast = fast.next
                count += 1

            return count

    return 0
