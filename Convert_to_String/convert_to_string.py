"""
Convert to String Lab 8
"""

class Node:

    """
    Docstring for Node
    """

    def __init__(self, data, n = None):
        self.data = data
        self.next = n


def stringify(node: Node) -> str | None:

    """
    Displays the sequence of linked nodes starting at given 'node' as string

    Examples:
    >>> Node(0, Node(1, Node(4, Node(9, Node(16)))))
    "0 -> 1 -> 4 -> 9 -> 16 -> None"
    """

    if not isinstance(node, Node):
        return None # wrong input

    s = []
    current = node
    while current is not None:
        s.append(str(current.data))
        current = current.next

    s.append("None")

    return " -> ".join(s)
