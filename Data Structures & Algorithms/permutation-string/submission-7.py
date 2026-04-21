class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        start = 0
        end = 0

        map1 = {}
        map2 = {}


        if len(s1) > len(s2):
            return False

        for s in s1:
            map1[s] = map1.get(s,0) + 1

        while end < len(s2):
            map2[s2[end]] = map2.get(s2[end],0) + 1

            if end - start + 1 == len(s1):
                if map1 == map2:
                    return True
                else:
                    map2[s2[start]] -= 1
                    if map2[s2[start]] == 0:
                        del map2[s2[start]]
                    start = start + 1

            end += 1

        return False
            
        