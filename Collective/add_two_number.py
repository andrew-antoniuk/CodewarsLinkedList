"""
Add Two Numbers LeetCode Lab 8
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
    Docst
    ring for Solution
    """

    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        """
        Docstring for addTwoNumbers
        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        """

        carry = 0
        res = ListNode(0)
        c = res

        while l1 or l2 or carry: # carry!
            l1_val = 0 if l1 is None else l1.val
            l2_val = 0 if l2 is None else l2.val

            current_val = (l1_val + l2_val + carry) % 10
            carry = (l1_val + l2_val + carry) // 10

            res_next = ListNode(current_val)
            res.next = res_next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            res = res.next

        return c.next
