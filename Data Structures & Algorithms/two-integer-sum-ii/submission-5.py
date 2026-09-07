class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        output = []

        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
                continue
            if numbers[l] + numbers[r] < target:
                l += 1
                continue
            if numbers[l] + numbers[r] == target:
                output.append(l+1)
                output.append(r+1)
                return output
        