class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0 and x%10==0):
            return False
        elif x==0:
            return True
        num=0
        origin=x
        while num<origin:
            num=num*10 + x%10
            x=x//10
        if num==origin and num%10!=0:
            return True
        else:
            return False