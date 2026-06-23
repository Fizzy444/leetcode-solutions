class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head is None:
            return head
        l = 0
        temp = head
        while temp:
            l += 1
            temp = temp.next
            
        if n == l:
            return head.next
        s = l - n
        temp = head
        prev = None
        for _ in range(s):
            prev = temp
            temp = temp.next
        prev.next = temp.next
        return head