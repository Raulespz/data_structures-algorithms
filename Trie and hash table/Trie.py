class Trie:

    class Node:

        def __init__(self):
            self.isEnd = False
            self.letters = [None] * 26  # [None, None, ..., None] - length: 26
            self.count = 0

    
    def __init__(self):
        self.__root = Trie.Node()

    def __convert(self, letter) -> int:
        return ord(letter.lower()) - ord('a')  # 0 .. 25
    
    def insert(self, word: str):
        currentNode = self.__root

        for letter in word:
            index = self.__convert(letter)
            if currentNode.letters[index] is None:
                newNode = Trie.Node()
                currentNode.letters[index] = newNode
                currentNode = newNode
            else:
                currentNode = currentNode.letters[index]

        currentNode.isEnd = True
        currentNode.count += 1


    def search(self, word: str) -> int:  # returns number of occurences of the searched word
        currentNode = self.__root

        for letter in word:
            index = self.__convert(letter)
            if currentNode.letters[index] is None:
                return 0
            currentNode = currentNode.letters[index]
        
        if currentNode.isEnd:
            return currentNode.count
        else:
            return 0


if __name__ == "__main__":
    trie = Trie()
    
    file = open("sample.txt", 'r')
    for line in file:
        words = line.split()
        for word in words:
            word = word.replace(',', '')
            word = word.replace('.', '')
            word = word.replace('/', '')
            word = word.replace('(', '')
            word = word.replace(')', '')
            word = word.replace('"', '')
            word = word.replace(';', '')
            word = word.replace('#', '')
            word = word.replace('2', '')
            word = word.replace('0', '')
            word = word.replace('1', '')
            word = word.replace('-', '')
            
            if word != "":
                trie.insert(word)
    
    print(trie.search("Python"))
