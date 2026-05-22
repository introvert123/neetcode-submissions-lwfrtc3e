class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        #look at the video 
        #logic is to either include the number (multiple times) and in the
        #other case not to include the number - to avoid duplicate combinations
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