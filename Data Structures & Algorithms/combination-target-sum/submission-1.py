class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []
        def dfs(i,sumOfNum):

            if sumOfNum == target:
                res.append(subset.copy())
                return

            if sumOfNum > target or i >= len(nums):
                return

            subset.append(nums[i])
            dfs(i,sumOfNum + nums[i])

            subset.pop()
            dfs(i+1,sumOfNum)
            

            
        dfs(0,0)
        return res