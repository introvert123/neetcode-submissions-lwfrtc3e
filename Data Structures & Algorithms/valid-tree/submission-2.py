class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        visit = set()
        adjList = defaultdict(list)

        for n1,n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        def cycle(i,prev):

            if i in visit:
                return True #cycle found

            visit.add(i)
            for num in adjList[i]:
                if prev != num: #e dont process such nodes which are prev/parent
                    if cycle(num,i):
                        return True

            return False


        if cycle(0,-1): #start node and parent node
            return False
        return len(visit) == n
        