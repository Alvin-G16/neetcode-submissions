class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            length=len(i)
            result += str(length) + "#" + i
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        p1 = 0

        while p1 < len(s):
            p2 = p1
            while s[p2] != "#":
                p2 += 1
            length = int(s[p1:p2])
            result.append(s[p2 + 1 : p2 + 1 + length]) # : is up to but NOT including hence no need for length -1 
            p1 = p2 + length + 1
        return result
