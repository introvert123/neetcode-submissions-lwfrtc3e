class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        subset = []

        nums.sort()

        def dfs(i):
            
            if i == len(nums):
                res.append(subset.copy())
                return 
                
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()

            #if the number that we are gng to see is the same num that we skipped then move ahead
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            dfs(i+1)
        
        dfs(0)
        return res
            

        