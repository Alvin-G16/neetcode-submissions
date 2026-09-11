class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = 0

        for r in range(len(nums)):
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])

            if r >= k - 1:
                output.append(q[0])

                if nums[l] == q[0]:
                    q.popleft()
                l += 1
        return output


        

