class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:


        start = 0
        end = 0

        minLen = float('inf')
        totalSum = 0
        length = 0


        while end < len(nums):
            totalSum += nums[end]

            while totalSum >= target:
                minLen = min(minLen, end - start + 1)
                totalSum -= nums[start]
                start += 1
            end += 1

        return 0 if minLen == float('inf') else minLen
            
        