class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        start = "0000"

        if start in deadends:
            return -1


        def children(lock):
            res = []
            for i in range(4):
                #adding 1 (taking 9 into consideration)
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])

                #sub 1(taking -1 into consideration)
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            
            return res
        
        #bfs is the right approach for the shortest/min turns reqd to open the lock
        queue = deque()
        queue.append(start)

        visited = set(deadends) #this will help in checking both visited and deadends
        turns  = 0

        while queue:

            size = len(queue)
            for _ in range(size):
                lock = queue.popleft()
                if lock == target:
                    return turns
                for child in children(lock):
                    if child not in visited:
                        visited.add(child)
                        queue.append(child)
            turns += 1


        return -1


        