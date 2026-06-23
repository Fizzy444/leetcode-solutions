# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return None
        temp = head
        l = 0
        while temp:
            l += 1
            temp = temp.next
        temp = head
        prev = None
        m = 0
        while m < l//2:
            prev = temp
            temp = temp.next
            m += 1
        prev.next = temp.next
        return head