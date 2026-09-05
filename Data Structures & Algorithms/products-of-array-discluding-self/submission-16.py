class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        beforeProduct = 1
        for i in range(len(nums)):
            result[i] = beforeProduct
            beforeProduct *= nums[i]

        afterProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= afterProduct
            afterProduct *= nums[i]
        return result