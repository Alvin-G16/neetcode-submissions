class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resultList = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            resultList[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            resultList[i] *= postfix
            postfix *= nums[i]
        return resultList
