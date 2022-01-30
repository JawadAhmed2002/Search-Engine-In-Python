import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'Data.txt')
def readFile(txtFile,dataType):
    with open(txtFile, mode='r') as f:
        data_content = f.read()
        data_content=data_content.split()
        f.close()
        if dataType=='movieId':
            return data_content[3::3]
        if dataType=='movieRating':
            return data_content[4::3]
        if dataType=='movieVoting':
            return data_content[5::3]

movieIds=readFile(my_file,'movieId')
movieRatings=readFile(my_file,'movieRating')
movieVotings=readFile(my_file,'movieVoting')

MovieRatings=[]
for i in movieRatings:
    MovieRatings.append((float(i)))


class Data:
    def __init__(self, dataValues):
        self.dataValues = dataValues

    def displayItem(self):
        print(self.dataValues)


class Data:
    def __init__(self, dataValues):
        self.dataValues = dataValues

    def displayItem(self):
        print(self.dataValues)


class Node:
    maxNumberofChildren = 4

    def __init__(self):
        self.numberOfItems = 0
        self.Parent = None
        self.childrenArray = []
        self.itemsArray = []
        for j in range(self.maxNumberofChildren):
            self.childrenArray.append(None)
        for k in range(self.maxNumberofChildren - 1):
            self.itemsArray.append(None)

    def connectChild(self, childNum, pChild):
        self.childrenArray[childNum] = pChild
        if pChild:
            pChild.Parent = self

    def disconnectChild(self, childNum):
        pTempNode = self.childrenArray[childNum]
        self.childrenArray[childNum] = None
        return pTempNode

    def getChild(self, childNum):
        return self.childrenArray[childNum]

    def getParent(self):
        return self.Parent

    def isLeaf(self):
        return not self.childrenArray[0]

    def getNumItems(self):
        return self.numberOfItems

    def getItem(self, index):
        return self.itemsArray[index]

    def isFull(self):
        return self.numberOfItems == self.maxNumberofChildren - 1

    def findItem(self, key):
        for j in range(self.maxNumberofChildren - 1):
            if not self.itemsArray[j]:
                break
            elif self.itemsArray[j].dataValues == key:
                return j
        return -1

    def insertItem(self, pNewItem):
        self.numberOfItems += 1
        newKey = pNewItem.dataValues

        for j in reversed(range(self.maxNumberofChildren - 1)):
            if self.itemsArray[j] == None:
                pass
            else:
                itsKey = self.itemsArray[j].dataValues
                if newKey < itsKey:
                    self.itemsArray[j + 1] = self.itemsArray[j]
                else:
                    self.itemsArray[j + 1] = pNewItem
                    return j + 1
        self.itemsArray[0] = pNewItem
        return 0

    def removeItem(self):

        pTemp = self.itemsArray[self.numberOfItems - 1]
        self.itemsArray[self.numberOfItems - 1] = None
        self.numberOfItems -= 1
        return pTemp

    def displayNode(self):
        for j in range(self.numberOfItems):
            self.itemsArray[j].displayItem()
        print()


class twothreefourTree:

    def __init__(self):
        self.root = Node()

    def find(self, key):
        parentNode = self.root
        while True:
            childNumber = parentNode.findItem(key)
            if childNumber != -1:
                return childNumber
            elif parentNode.isLeaf():
                return -1
            else:
                parentNode = self.getNextChild(parentNode, key)

    def insert(self, dValue):
        parentNode = self.root
        pTempItem = Data(dValue)

        while True:
            if parentNode.isFull():
                self.split(parentNode)
                parentNode = parentNode.getParent()
                parentNode = self.getNextChild(parentNode, dValue)
            elif parentNode.isLeaf():
                break
            else:
                parentNode = self.getNextChild(parentNode, dValue)
        parentNode.insertItem(pTempItem)

    def split(self, pThisNode):
        pItemC = pThisNode.removeItem()
        pItemB = pThisNode.removeItem()
        pChild2 = pThisNode.disconnectChild(2)
        pChild3 = pThisNode.disconnectChild(3)
        pNewRight = Node()
        if pThisNode == self.root:
            self.root = Node()
            pParent = self.root
            self.root.connectChild(0, pThisNode)
        else:
            pParent = pThisNode.getParent()
        itemIndex = pParent.insertItem(pItemB)
        n = pParent.getNumItems()
        j = n - 1
        while j > itemIndex:
            pTemp = pParent.disconnectChild(j)
            pParent.connectChild(j + 1, pTemp)
            j -= 1
        pParent.connectChild(itemIndex + 1, pNewRight)
        pNewRight.insertItem(pItemC)
        pNewRight.connectChild(0, pChild2)
        pNewRight.connectChild(1, pChild3)

    def getNextChild(self, pNode, theValue):
        numItems = pNode.getNumItems()
        for j in range(numItems):
            if theValue < pNode.getItem(j).dataValues:
                return pNode.getChild(j)
        else:
            return pNode.getChild(j + 1)

    def displayTree(self):
        self.recDisplayTree(self.root, 0, 0)

    def recDisplayTree(self, pThisNode, level, childNumber):
        print('level=', level, 'child=', childNumber)
        pThisNode.displayNode()
        numItems = pThisNode.getNumItems()
        for j in range(numItems + 1):
            pNextNode = pThisNode.getChild(j)
            if pNextNode:
                self.recDisplayTree(pNextNode, level + 1, j)
            else:
                return

SearchEngine=twothreefourTree()
print('Wait For the Data To Load In The 234 Tree and Then it will display: ')
for i in range(len(MovieRatings)//2):
    SearchEngine.insert(MovieRatings[i])
SearchEngine.displayTree()

