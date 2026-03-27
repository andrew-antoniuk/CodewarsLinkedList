"""
Swap Nodes LeetCode Lab 8
"""

from typing import Optional

class ListNode:

    """
    Docstring for ListNode
    """

    def __init__(self, val = 0, n = None):
        self.val = val
        self.next = n

class Solution:

    """
    Docstring for Solution
    """

    def swap_pairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Docstring for swap_pairs
        Input: head = [1,2,3,4]
        Output: [2,1,4,3]
        """

        prev_head = ListNode(0, head)
        previous = prev_head
        current = head

        while current is not None and current.next is not None: # pair check
            first = current
            second = current.next

            previous.next = second
            first.next = second.next

            # complete the swap
            second.next = first

            # move forward
            previous = first
            current = first.next

        return prev_head.next
