from LinkStack import *

class Tree234:

    maxLinks = 4 # Maximum number of children of a node
    maxKeys = maxLinks - 1 # Maximum number of keys in a node

    class __Node:

        def __init__(self, key, data, *children):
            if len(children) not in (0, 2): # A new node is created in the splitting phase. A new node always must have 0 or 2 children.
                raise ValueError("2-3-4 tree nodes must be created with 0 or 2 children")
            
            valid = [x
                     for x in children
                     if isinstance(x, type(self))]

            self.nKeys = 1 # Currently stored number of keys
            self.keys = [key] * Tree234.maxKeys # [key, _, _]
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
        nKeys = self.__root.nKeys # Number of keys in the root
        return (self.__root.data[:nKeys], self.__root.keys[:nKeys]) # Returns all data and keys stored in the root
    
    def __find(self, goal, current, parent, prepare=True): # goal: key what we want to find
        # goal: key what we want to find
        # current: node where we are currently
        # parent: parent node of the current
        # prepare: True if we want to insert sth, splitting can be made
        if current is None:
            return (current, parent) # (None, parent)
        
        # Searches the first key in the current node which is not less than the goal
        i = 0
        while (i < current.nKeys and current.keys[i] < goal):
            i += 1

        # Goal is found in the tree
        if i < current.nKeys and goal == current.keys[i]:
            return (current, parent) # Returns (current node, parent node of the current node)
        
        
        if (prepare and current.nKeys == Tree234.maxKeys): # A full node is found => The node must be splitted
            current, parent = self.__splitNode(current, parent, goal)
            i = 0 if goal < current.keys[0] else 1 # We decide where to countinue the find process
        return ((prepare and current, parent) if current.isLeaf() else self.__find(goal, current.children[i], current, prepare))
    
    def __splitNode(self, toSplit, parent, goal):
        # toSplit: the node what we want to split
        # parent: parent node of toSplit
        # goal: key what we are searching for or want to insert

        if toSplit.isLeaf():
            newNode = self.__Node(toSplit.keys[2], toSplit.data[2])
        else:
            newNode = self.__Node(toSplit.keys[2], toSplit.data[2], *toSplit.children[2:toSplit.nChild])
        
        toSplit.nKeys = 1
        toSplit.nChild = max(0, toSplit.nChild - 2) # For a leaf: 0, for a non-leaf: 2
        
        if parent is self: # We want to split the root
            self.__root = self.__Node(toSplit.keys[1], toSplit.data[1], toSplit, newNode) # toSplit and newNode will be the two children of the new root
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
            if p is self: # The tree is empty
                self.__root = self.__Node(key, value)
                return True
            raise Exception("__find did not find 2-3-4 node for insertion")
        return node.insertKeyValue(key, value)

    def traverse(self, traverseType="in"):
        # Verify traversal type is an accepted value
        if traverseType not in ["pre", "in", "post"]:
            raise ValueError(f"Unknown traversal type: {traverseType}")

        stack = LinkStack()
        stack.push(self.__root)

        while not stack.isEmpty():
            item = stack.pop()
            if isinstance(item, self.__Node):
                last = max(item.nChild, item.nKeys + (1 if traverseType == "post" else 0))
                for c in range(last - 1, -1, -1):
                    if traverseType == "post" and 0 < c and c - 1 < item.nKeys:
                        stack.push((item.keys[c - 1], item.data[c - 1]))
                    if traverseType == "in" and c < item.nKeys:
                        stack.push((item.keys[c], item.data[c]))
                    if c < item.nChild:
                        stack.push(item.children[c])
                    if traverseType == "pre" and c < item.nKeys:
                        stack.push((item.keys[c], item.data[c]))
            else:
                yield item

if __name__ == "__main__":
    tree = Tree234()
    tree.insert(5, "Five")
    tree.insert(3, "Three")
    tree.insert(31, "Thirty one")
    tree.insert(24, "Twenty four")
    tree.insert(36, "Thirty six")
    tree.insert(2, "Two")
    tree.insert(6, "Six")
    tree.insert(2, "Zwei")
    tree.insert(4, "Four")

    # traversalItems = tree.traverse("pre")
    # for item in traversalItems:
    #     print(item)

    # print(tree.search(7))
    print(tree.root())

