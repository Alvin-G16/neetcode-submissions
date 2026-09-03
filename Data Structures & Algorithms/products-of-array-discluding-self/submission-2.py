class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []

        for i in range(len(nums)):

            result_list = []
            for n in nums:
                result_list.append(n)
            result_list.remove(nums[i])

            result = 1
            for k in result_list:
                result = result * k
            output.append(result)
            result = 1
            result_list.clear()

        return output
        