

class BinarySearchTree:

    class __Node:
        def __init__(self, key, data, left=None, right=None):
            self.key = key
            self.data = data
            self.leftChild = left
            self.rightChild = right

        def __str__(self):
            return (f"({self.key}, {self.data})")
        
    def __init__(self):
        self.__root = None

    def isEmpty(self):
        return self.__root == None
    
    def root(self):
        if self.isEmpty():
            raise Exception("No root node in empty tree")
        return (self.__root.key, self.__root.data)
    
    def __find(self, goal):
        current = self.__root
        parent = self

        while current and goal != current.key:
            parent = current
            current = current.leftChild if goal <= current.key else current.rightChild # ternary operator
            # if goal <= current.key:
            #     current = current.leftChild
            # else:
            #     current = current.rightChild

        return (current, parent) # parent: the parent node of the current node
    
    def search(self, goal):
        node, _ = self.__find(goal)
        return node.data if node else None # ternary operator
    
    def insert(self, key, data):
        node, parent = self.__find(key)

        if node:
            node.data = data
            return False

        if parent is self:
            self.__root = self.__Node(key, data)
        elif key < parent.key:
            parent.leftChild = self.__Node(key, data, left=node)
        else:
            parent.rightChild = self.__Node(key, data, right=node)

        return True

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(3, "John Doe")
    bst.insert(5, "Susan Smith")
    bst.insert(1, "David Doodle")

    print(bst.search(2))