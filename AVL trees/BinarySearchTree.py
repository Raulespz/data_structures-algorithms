from LinkStack import *

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
    
    def inOrderTraverse(self, function=print):
        self.__inOrderTraverse(self.__root, function)

    def __inOrderTraverse(self, node, function):
        if node:
            self.__inOrderTraverse(node.leftChild, function)
            function(node)
            self.__inOrderTraverse(node.rightChild, function)

    def traverse_rec(self, traverseType="in"): # in, pre, post
        if traverseType in ["pre", "in", "post"]:
            return self.__traverse(self.__root, traverseType)
        
        raise ValueError(f"Unknown traversal type: {traverseType}")
    
    def __traverse(self, node, traverseType):
        if node is None:
            return
        if traverseType == "pre":
            yield (node.key, node.data)
        for childKey, childData in self.__traverse(node.leftChild, traverseType):
            yield (childKey, childData)
        if traverseType == "in":
            yield (node.key, node.data)
        for childKey, childData in self.__traverse(node.rightChild, traverseType):
            yield (childKey, childData)
        if traverseType == "post":
            yield (node.key, node.data)

    def traverse(self, traverseType="in"):
        if traverseType not in ["pre", "in", "post"]:
            raise ValueError(f"Unknown traversal type: {traverseType}")
        
        stack = Stack()
        stack.push(self.__root)

        while not stack.isEmpty():
            item = stack.pop()
            if isinstance(item, self.__Node):
                if traverseType == "post":
                    stack.push((item.key, item.data))
                stack.push(item.rightChild)
                if traverseType == "in":
                    stack.push((item.key, item.data))
                stack.push(item.leftChild)
                if traverseType == "pre":
                    stack.push((item.key, item.data))
            elif item: # item is not None
                yield item

    def minNode(self):
        if self.isEmpty():
            raise Exception("No minimum node in empty tree")
        
        node = self.__root

        while node.leftChild:
            node = node.leftChild

        return (node.key, node.data)
    
    def delete(self, goal):
        node, parent = self.__find(goal)
        if node is not None:
            return self.__delete(parent, node)
        
    def __delete(self, parent, node): # node is not None
        deleted = (node.key, node.data)

        if node.leftChild: # node has left child
            if node.rightChild: # node has both childre
                self.__promote_successor(node)
            else: # no right child
                if parent is self: # root is deleted
                    self.__root = node.leftChild
                elif parent.leftChild is node:
                    parent.leftChild = node.leftChild
                else:
                    parent.rightChild = node.leftChild
        else: # node has no left child
            if parent is self:
                self.__root = node.rightChild
            elif parent.leftChild is node:
                parent.leftChild = node.rightChild
            else: parent.rightChild = node.rightChild

        return deleted
    
    def __promote_successor(self, node):
        successor = node.rightChild
        parent = node

        while successor.leftChild:
            parent = successor
            successor = successor.leftChild

        node.key = successor.key
        node.data = successor.data
        self.__delete(parent, successor)

    def levels(self):
        return self.__levels(self.__root)
    
    def __levels(self, node):
        if not node:
            return 0
        
        return 1 + max(self.__levels(node.leftChild), self.__levels(node.rightChild))
    
    def nodes(self):
        count = 0
        for _, _ in self.traverse():
            count += 1
        return count
    
    def print(self, indentBy=4):
        self.__pTree(self.__root, "Root:    ", "", indentBy)

    def __pTree(self, node, nodeType, indent, indentBy=4):
        if node:
            self.__pTree(node.rightChild, "RIGHT:   ", indent + " " * indentBy, indentBy)
            print(indent + nodeType, node)
            self.__pTree(node.leftChild, "LEFT:    ", indent + " " * indentBy, indentBy)

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(3, "John Doe")
    bst.insert(5, "Susan Smith")
    bst.insert(1, "David Doodle")
    bst.insert(2, "Two Two")
    bst.insert(4, "Four Four")
    bst.print()

    # bst.delete(3)
    # bst.inOrderTraverse()
    # print(bst.levels())
    # print(bst.nodes())