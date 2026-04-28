class Node:
    def __init__(self):
        self.isLastLetter = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Node()

        

    def addWord(self, word: str) -> None:
        
        current = self.root


        for letter in word:
            if letter not in current.children:
                current.children[letter] = Node()
            
            current = current.children[letter]
        
        current.isLastLetter = True

        

    def search(self, word: str) -> bool:

        def dfs(index, current_node):
            current = current_node


            # we go thru every character in the node, via index

            for i in range(index, len(word)):
                current_letter = word[i]


                if current_letter == ".":


                    for branchNode in current.children.values():
                        if dfs(i + 1, branchNode):
                            return True
                    return False
                
                # this assume that it is not a . (aka the wildcard)



                else:
                    if word[i] not in current.children:
                        return False

                    current = current.children[word[i]]
                
            return current.isLastLetter
        
        return dfs(0,self.root)














        
