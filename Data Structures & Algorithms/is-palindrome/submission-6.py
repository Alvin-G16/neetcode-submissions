class Solution:
    def isPalindrome(self, s: str) -> bool:
        sAlnum = ""

        for l in s:
            if l.isalnum():
                sAlnum += l.lower()
        return sAlnum == sAlnum[::-1]
        