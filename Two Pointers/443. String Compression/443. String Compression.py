class Solution(object):
    def compress(self, chars):
        res = []
        count = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                res.append(chars[i-1])
                if count > 1:
                    for c in str(count):
                        res.append(c)
                count = 1
        res.append(chars[-1])
        if count > 1:
            for c in str(count):
                res.append(c)
        for i in range(len(res)):
            chars[i] = res[i]
        return len(res)