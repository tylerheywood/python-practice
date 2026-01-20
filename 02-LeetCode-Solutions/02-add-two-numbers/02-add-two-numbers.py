# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list (from leetcode)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()       # placeholder head
        current = dummy          # pointer for building output
        carry = 0                # carry from addition

        # loop until both lists are exhausted and no carry remains
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # compute sum + carry
            total = v1 + v2 + carry
            carry = total // 10          # update carry for next digit
            digit = total % 10            # current digit

            # append result digit to output
            current.next = ListNode(digit)
            current = current.next

            # advance l1 / l2 if present
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # return the next of dummy (skips the placeholder)
        return dummy.next

