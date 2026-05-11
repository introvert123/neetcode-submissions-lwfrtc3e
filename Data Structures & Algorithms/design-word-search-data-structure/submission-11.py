class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:

        curr = self.root

        for ch in word:
            idx = ord(ch) - ord('a')

            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        
        curr.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(curr,i):

            if i == len(word):
                return curr.endOfWord
            ch = word[i]

            if ch == '.':
                for child in curr.children:
                    if child and dfs(child,i+1):
                        return True
                return False
            else:
                idx = ord(ch) - ord('a')
                if curr.children[idx] == None:
                    return False
                return dfs(curr.children[idx],i+1)

        return dfs(self.root,0)
