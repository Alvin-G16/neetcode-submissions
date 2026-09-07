class Solution:
    def isPalindrome(self, s: str) -> bool:
        sAlnum = ""

        for l in s:
            if self.alphaNum(l) == True:
                sAlnum += l.lower()
        return sAlnum == sAlnum[::-1]
    
    def alphaNum(self, c: str) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
        