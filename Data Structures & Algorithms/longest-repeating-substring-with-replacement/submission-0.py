class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        maxLen = 0
        start = 0
        end = 0

        count = {}

        while end < len(s):

            count[s[end]] = count.get(s[end],0) + 1
            winLen = end - start + 1

            while winLen - max(count.values()) > k:
                count[s[start]] -= 1
                start += 1
                winLen -= 1
            maxLen = max(maxLen, winLen)
            end += 1
        
        return maxLen