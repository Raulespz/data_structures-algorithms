from LinkStack import *

class TowerOfHanoi:
    def __init__(self, nDisks):
        self.__stacks = [None] * 3
        self.__labels = ['L', 'M', 'R']
        self.__nDisks = nDisks
        self.reset()

    def reset(self):
        for spindle in range(3):
            self.__stacks[spindle] = LinkStack()
            if spindle == 0:
                for disk in range(self.__nDisks, 0, -1): # nDisks, nDisks - 1, nDisks - 2, ..., 2, 1
                    self.__stacks[spindle].push(disk)

    def getLabel(self, spindle):
        return self.__labels[spindle]
    
    def getHeight(self, spindle):
        return len(self.__stacks[spindle])
    
    def getTopDisk(self, spindle):
        currentStack = self.__stacks[spindle]
        if not currentStack.isEmpty():
            return currentStack.peek()
        
    def move(self, source, target, show=False):
        sourceStack = self.__stacks[source]
        targetStack = self.__stacks[target]
        if sourceStack.isEmpty():
            raise Exception(f"Cannot move from empty spindle {self.getLabel(source)}")
        if not targetStack.isEmpty() and self.getTopDisk(source) > self.getTopDisk(target):
            raise Exception(f"Cannot move disk {self.getTopDisk(source)} on top of disk {self.getTopDisk(target)}")
        movingDisk = sourceStack.pop()
        targetStack.push(movingDisk)
        if show:
            print(f"Move disk {self.getTopDisk(target)} from spindle {self.getLabel(source)} to {self.getLabel(target)}")

    def solve(self, nDisks=None, start=0, target=2, spare=1, show=False):
        if nDisks == None:
            nDisks = self.getHeight(start)
        if nDisks <= 0:
            return
        if self.getHeight(start) < nDisks:
            raise Exception(f"Not enough disks ({nDisks}) on starting spindle {self.getLabel(start)}")
        
        self.solve(nDisks - 1, start, spare, target, show)
        self.move(start, target, show)
        self.solve(nDisks - 1, spare, target, start, show)

if __name__ == "__main__":
    TowerOfHanoi(4).solve(show=True)