class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adjList = defaultdict(list)
        visited = set()
        count = 0

        for n1,n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        def dfs(i):
            
            visited.add(i)
            for val in adjList[i]:
                if val not in visited:
                    dfs(val)


        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count

        