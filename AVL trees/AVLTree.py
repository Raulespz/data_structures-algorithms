class AVLTree:

    class __Node:
        def __init__(self, key, data):
            self.key = key
            self.data = data
            self.leftChild = None
            self.rightChild = None
            self.updateHeight()

        def updateHeight(self):
            leftHeight = self.leftChild.height if self.leftChild is not None else 0
            rightHeight = self.rightChild.height if self.rightChild is not None else 0
            self.height = 1 + max(leftHeight, rightHeight)

        def heightDiff(self):
            leftHeight = self.leftChild.height if self.leftChild is not None else 0
            rightHeight = self.rightChild.height if self.rightChild is not None else 0
            return leftHeight - rightHeight # positive if height of left child is more than height of right child

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

    def insert(self, key, data):
        self.__root, flag = self.__insert(self.__root, key, data)
        return flag
    
    def __insert(self, node, key, data): # recursive insertion
        if node is None: # first item is inserted, it will be the root of the tree
            return self.__Node(key, data), True

        if key == node.key: # update the data of the node
            node.data = data
            return node, False

        if key < node.key: # insert to the left subtree
            node.leftChild, flag = self.__insert(node.leftChild, key, data)
            if node.heightDiff() > 1:
                if node.leftChild.key < key:
                    node.leftChild = self.rotateLeft(node.leftChild)
                node = self.rotateRight(node)
        else: # key > node.key
            node.rightChild, flag = self.__insert(node.rightChild, key, data)
            if node.heightDiff() < -1:
                if key < node.rightChild.key:
                    node.rightChild = self.rotateRight(node.rightChild)
                node = self.rotateLeft(node)

        node.updateHeight()
        return node, flag

    def rotateLeft(self, top):
        toRaise = top.rightChild
        top.rightChild = toRaise.leftChild
        toRaise.leftChild = top
        top.updateHeight()
        toRaise.updateHeight()
        return toRaise

    def rotateRight(self, top):
        toRaise = top.leftChild
        top.leftChild = rightChild.toRaise
        toRaise.rightChild = top
        top.updateHeight()
        toRaise.updateHeight
        return toRaise

    def print(self, indentBy=4):
        self.__pTree(self.__root, "Root:    ", "", indentBy)

    def __pTree(self, node, nodeType, indent, indentBy=4):
        if node:
            self.__pTree(node.rightChild, "RIGHT:   ", indent + " " * indentBy, indentBy)
            print(indent + nodeType, node)
            self.__pTree(node.leftChild, "LEFT:    ", indent + " " * indentBy, indentBy)

    def delete(self, goal): # we want to delete the node with key which is eqaul to goal
        self.__root, flag = self.__delete(self.__root, goal)
        return flag

    def __delete(self, node, goal):
        if node is None:
            return None, False

        if goal < node.key:
            node.leftChild, flag = self.__delete(node.leftChild, goal)
            node = self.__balanceLeft(node)

        elif: goal > node.key:
            node.rightChild, flag = self.__delete(node.rightChild, goal)
            node = self.__balanceRight(node)

        elif node.leftChild is None:
            return node.rightChild, True
        elif node.rightChild is None:
            return node.leftChild, True
        else:
            node.key, node.data, node.rightChild = self.__deleteMin(node.rightChild)
            node = self.__balanceRight(node)
            flag = True

    def __deleteMin(self, node):
        if node.leftChild is None:
            return node.key, node.data, node.rightChild
        
        key, data, node.leftChild = self.__deleteMin(self, node.leftChild)
        node = self.__balanceLeft(node)
        node.updateHeight()
        return key, data, node

    def __balanceLeft(self, node):
        if node.heightDiff() < -1:
            if node.rightChild.heightDiff() > 0:
                node.rightChild = self.rotateRight(node.rightChild)
            node = self.rotateLeft(node)
        return node

    def __balanceRight(self, node):
        if node.heightDiff() > 1:
            if node.leftChild.heightDiff < 0:
                node.leftChild = self.rotateLeft(node.leftChild)
            node = self.rotateRight(node)
        return node
        

if __name__ == "__main__":
    tree = AVLTree()

    tree.insert(50, 50)
    tree.insert(60, 60)
    tree.insert(70, 70)
    tree.insert(80, 80)
    tree.insert(90, 90)
    tree.print()

    