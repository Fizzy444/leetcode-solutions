# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        l = []
        temp = head
        while temp:
            l.append(temp.val)
            temp = temp.next
        if l == l[::-1]:
            return True
        return False