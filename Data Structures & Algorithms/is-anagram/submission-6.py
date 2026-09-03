class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        else:
            dict1 = {}
            dict2 = {}

            for i in s:
                if i in dict1:
                    dict1[i] = dict1[i] + 1
                else:
                    dict1[i] = 1

            for k in t:
                if k in dict2:
                    dict2[k] = dict2[k] + 1
                else:
                    dict2[k] = 1

        return dict1 == dict2