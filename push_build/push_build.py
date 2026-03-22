"""
Docstring for CodewarsLinkedList.push_build.push_build
"""

from CodewarsLinkedList.preloaded import Node


def push(head, data):

    """
    Docstring for push
    """

    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():

    """
    Docstring for build_one_two_three
    """

    chained = None

    chained = push(chained, 3)
    chained = push(chained, 2)
    chained = push(chained, 1)

    return chained
