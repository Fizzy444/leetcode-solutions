class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for c in ransomNote:
            if c in magazine:
                magazine = magazine.replace(c, "", 1)
            else:
                return False
        return True