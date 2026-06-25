# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        s = 0
        temp = head
        while temp:
            s += 1
            temp = temp.next
        m = 0
        temp = head
        while m < s//2:
            temp = temp.next
            m += 1
        return temp