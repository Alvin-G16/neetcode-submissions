class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {"(" : ")", "[" : "]", "{" : "}"}

        for char in s:
            if char in openToClose:
                stack.append(char)
            else:
                if stack and openToClose[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
        