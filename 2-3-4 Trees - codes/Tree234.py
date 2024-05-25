class Tree234:

    maxLinks = 4
    maxKeys = maxLinks - 1

    class __Node:

        def __init__(self, key, data, *children):
            if len(children) not in (0, 2):
                raise ValueError("2-3-4 tree nodes must be created with 0 or 2 children")
            
            valid = [x
                     for x in children
                     if isinstance(x, type(self))]

            self.nKeys = 1
            self.keys = [key] * Tree234.maxKeys
            self.data = [data] * Tree234.maxKeys
            self.nChild = len(valid)
            self.children = (valid + [None] * (Tree234.maxLinks - len(valid)))

        def __str__(self):
            return "<Node234 " + "-".join(str(k) for k in self.keys[:self.nKeys]) + ">"
        
        def isLeaf(self):
            return self.nChild == 0
        
        def insertKeyValue(self, key, data, subtree=None):
            i = 0
            while i < self.nKeys and self.keys[i] < key:
                i += 1
            if i == Tree234.maxKeys:
                raise Exception("Cannot insert key into full 2-3-4 node")
            if self.keys[i] == key:
                self.data[i] = data
                return False
            j = self.nKeys
            if j == Tree234.maxKeys:
                raise Exception("Cannot insert key into full 2-3-4 node")
            while i < j:
                self.keys[j] = self.keys[j - 1]
                self.data[j] = self.data[j - 1]
                self.children[j] = self.children[j - 1]
                j -= 1
            self.keys[i] = key
            self.data[i] = data
            self.nKeys += 1
            if subtree:
                self.children[i + 1] = subtree
                self.nChild += 1
            return True
        
    def __init__(self):
        self.__root = None
    
    def isEmpty(self):
        return self.__root is None
    
    def root(self):
        if self.isEmpty():
            raise Exception("No root node in empty tree")
        nKeys = self.__root.nKeys
        return (self.__root.data[:nKeys], self.__root.keys[:nKeys])
    
    def __find(self, goal, current, parent, prepare=True):
        if current is None:
            return (current, parent)
        i = 0
        while (i < current.nKeys and current.keys[i] < goal):
            i += 1
        if i < current.nKeys and goal == current.keys[i]:
            return (current, parent)
        if (prepare and current.nKeys == Tree234.maxKeys):
            current, parent = self.__splitNode(current, parent, goal)
            i = 0 if goal < current.keys[0] else 1
        return ((prepare and current, parent) if current.isLeaf() else self.__find(goal, current.children[i], current, prepare))
    
    def __splitNode(self, toSplit, parent, goal):
        if toSplit.isLeaf():
            newNode = self.__Node(toSplit.keys[2], toSplit.data[2])
        else:
            newNode = self.__Node(toSplit.keys[2], toSplit.data[2], *toSplit.children[2:toSplit.nChild])
        toSplit.nKeys = 1
        toSplit.nChild = max(0, toSplit.nChild - 2)
        if parent is self:
            self.__root = self.__Node(toSplit.keys[1], toSplit.data[1], toSplit, newNode)
            parent = self.__root
        else:
            parent.insertKeyValue(toSplit.keys[1], toSplit.data[1], newNode)
        return (toSplit if goal < toSplit.keys[1] else newNode, parent)
    
    def search(self, goal):
        node, p = self.__find(goal, self.__root, self, prepare=False)
        if node:
            return node.data[0 if node.nKeys < 2 or goal < node.keys[1] else 1 if goal == node.keys[1] else 2]
        
    def insert(self, key, value):
        node, p = self.__find(key, self.__root, self, prepare=True)
        if node is None:
            if p is self:
                self.__root = self.__Node(key, value)
                return True
            raise Exception("__find did not find 2-3-4 node for insertion")
        return node.insertKeyValue(key, value)
