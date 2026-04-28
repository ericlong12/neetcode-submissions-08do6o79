class Node:
    def __init__(self):
        self.children = {} #key = letter.    value = Node()
        self.isLastLetter = False



class PrefixTree:

    def __init__(self):
        self.root = Node()

        

    def insert(self, word: str) -> None:

        current = self.root

        for character in word:
            # we want to insert it to the tree
            if character not in current.children:
                current.children[character] = Node()
            current = current.children[character]

        current.isLastLetter = True
                


    def search(self, word: str) -> bool:

        current = self.root

        for character in word:
            if character not in current.children:
                return False
            
            #this line assumes it been found
            current = current.children[character]

        return current.isLastLetter





        

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for character in prefix:
            if character not in current.children:
                return False
            
            #this line assumes it been found
            current = current.children[character]

        return True

        
        