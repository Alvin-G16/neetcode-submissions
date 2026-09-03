class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = s.replace(" ", "")
        formatted = formatted.replace("?", "")
        formatted = formatted.replace("!", "")
        formatted = formatted.replace(".", "")
        formatted = formatted.replace(",", "")
        formatted = formatted.replace("'", "")
        formatted = formatted.replace(":", "")
        rev = formatted[::-1]
        
        return formatted.lower() == rev.lower()
        