from math import floor
from math import log2
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
for i in range(0,len(movieRatings)):
        movieRatings[i] = float(movieRatings[i])
# Movie_Data={}
# for index in range(len(movieIds)):
#     Movie_Data[movieIds[index]]=movieRatings[index]
# Id_list = list(Movie_Data.keys())
# Rating_list = list(Movie_Data.values())
# print(Movie_Data)
# position = Rating_list.index('5.6')
# print(Id_list[position])
# IntMovieRatings=[]
# for i in movieRatings:
#     IntMovieRatings.append(int(float(i)*10))
# print(IntMovieRatings)
# print(movieVotings[0],movieIds[0],movieRatings[0])
# print(len(movieRatings),len(movieVotings),len(movieIds))
movieRatings.sort()
# for i in range(99):
#     print(movieIds[i],type(float(movieRatings[i])),movieVotings[i])
# def Movie_Data(rating):
#     singlemovieData=[]
#     len_Of_data=len(movieRatings)

class Node:
    def __init__(self, mId, mRating, mVoting):
        self.mId=mId
        self.mRating=mRating
        self.mVoting=mVoting
        self.left = None
        self.right = None
        self.height = 1
    def printData(self):
        print('Movie Id Is: ',self.mId,'Movie Rating Is: ',self.mRating,'Movie Voting Is: ',self.mVoting)
    def getRating(self):
        return self.mRating
    def getVoting(self):
        return self.mVoting
    def getId(self):
        return self.mId

class AVLTree:
    def __init__(self):
        self.root = None
    def Max(self, a, b):
        if a > b:
            return a
        return b
    def getHeight(self, root):
        if root == None:
            return 0
        return root.height

    def getBalanceFactor(self, root):
        if root == None:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def lowestValue(self, root):
        if root is None or root.left is None:
            return root
        return self.lowestValue(root.left)

    def insert(self, root, mId, mRating, mVoting):
        newNode=Node(mId, mRating, mVoting)
        if root == None:
            return newNode
        elif newNode.mRating < root.mRating:
            root.left = self.insert(root.left,mId, mRating, mVoting)
        else:
            root.right = self.insert(root.right,mId, mRating, mVoting)
        # return root
        # Update Height
        root.height = 1 + self.Max(self.getHeight(root.left), self.getHeight(root.right))
        balanceFactor = self.getBalanceFactor(root)

        # left left violaion:
        if balanceFactor > 1 and root.left.mRating > newNode.mRating:
            return self.rightRotate(root)

        # right right violation:
        if balanceFactor < -1 and root.right.mRating <= newNode.mRating:
            return self.leftRotate(root)

        # left right violation:
        if balanceFactor > 1 and root.left.mRating < newNode.mRating:
            if root.left!=None:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        # right left violation:
        if balanceFactor < -1 and root.right.mRating > newNode.mRating:
            if root.right!=None:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    def rightRotate(self, node):
        leftOfRoot = node.left
        rightOfLeft = leftOfRoot.right
        leftOfRoot.right = node
        node.left = rightOfLeft
        node.height = 1 + self.Max(self.getHeight(node.left), self.getHeight(node.right))
        leftOfRoot.height = 1 + self.Max(self.getHeight(leftOfRoot.left), self.getHeight(leftOfRoot.right))
        return leftOfRoot

    def leftRotate(self, node):
        rightOfRoot = node.right
        leftOfRight = rightOfRoot.left
        rightOfRoot.left = node
        node.right = leftOfRight
        node.height = 1 + self.Max(self.getHeight(node.left), self.getHeight(node.right))
        rightOfRoot.height = 1 + self.Max(self.getHeight(rightOfRoot.left), self.getHeight(rightOfRoot.right))
        return rightOfRoot

    def inOrderTraversal(self, root):
        # left -> root -> right
        if not root:
            return
        self.inOrderTraversal(root.left)
        root.printData()
        self.inOrderTraversal(root.right)

    def preOrderTraversal(self, root):
        # root -> left -> right
        if not root:
            return
        root.printData()
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)

    def postOrderTraversal(self, root):
        # left -> right -> root
        if not root:
            return
        self.postOrderTraversal(root.left)
        self.postOrderTraversal(root.right)
        root.printData()

    def SimilarRatingsLen(self,root):
        ratingList=[1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,
                    3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4.0,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,5.0,
                    5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,6.0,6.1,6.2,6.3,6.4,6.5,6.6,6.7,6.8,6.9,7.0,
                    7.1,7.2,7.3,7.4,7.5,7.6,7.7,7.8,7.9,8.0,8.1,8.2,8.3,8.4,8.5,8.6,8.7,8.8,8.9,9.0,
                    9.1,9.2,9.3,9.4,9.5,9.6,9.7,9.8,9.9,10.0]
        for i in range(len(ratingList)):
            print(self.SearchForSimilar(root,ratingList[i],''))

    def SearchForSimilar(self, root, mRating, Treevalue):
        if Treevalue == True:
            return True
        if root.left != None:
            Treevalue = self.SearchForSimilar(root.left, mRating, Treevalue)
        if root.mRating == mRating:
            print(root.getRating(),root.getId(),root.getVoting())
            return True
        if root.right != None:
            Treevalue = self.SearchForSimilar(root.right, mRating, Treevalue)
        return Treevalue

    def Search(self, root, mRating, Treevalue):
        # DataFounded=[]
        if Treevalue == True:
            return True
        if root.left != None:
            Treevalue = self.Search(root.left, mRating, Treevalue)
        if root.mRating == mRating:
            print('The Movie Id, Rating and Voting is: ')
            # DataFounded.append(root.printData())
            root.printData()
            return True
        if root.right != None:
            Treevalue = self.Search(root.right, mRating, Treevalue)
        return Treevalue


def AVLsearchEngineMenu():
    print('Wait For Data To Load In The Tree:...........')
    print()
    SearchEngine=AVLTree()
    lenOfData=len(movieRatings)
    for i in range(lenOfData):
        SearchEngine.root = SearchEngine.insert(SearchEngine.root, movieIds[i],
                                            movieRatings[i], movieVotings[i])
    print('Data Loaded in Tree Successfullly:')
    while True:
        print('Menu to Perform Operations on Search Engine Based On AVL Tree:')
        print('a. Most Popular Movies In the Given Data Are: ')
        print('b. Least Popular Movies In the Given Data Are: ')
        print('c. Similar Rating Movies In the Given Data Are: ')
        print('d. Print All Data In The Tree Based On AVL Tree: ')
        print('e. Exit The Program')
        Command=input('Enter any above alphabet to perform operations: ')
        print()
        if Command=='a':
            print('Most Popular Movies Are Following:')
            SearchEngine.Search(SearchEngine.root,10.0,'')

        if Command=='b':
            print('Least Popular Movies Are Following:')
            SearchEngine.Search(SearchEngine.root,1.0,'')

        if Command=='c':
            print('Similar Rating Movies Are Following:')
            SearchEngine.SimilarRatingsLen(SearchEngine.root)


        if Command=='d':
            print('All The Data In The Tree Is Following:')
            SearchEngine.preOrderTraversal(SearchEngine.root)

        if Command=='e':
            print('Program Exit Successfully')
            return quit()

Search1=AVLsearchEngineMenu()


# SearchEngine=AVLTree()
#
# for i in range(len(movieRatings)):
#     SearchEngine.root=SearchEngine.insert(SearchEngine.root,movieIds[i],movieRatings[i],movieVotings[i])
#
# SearchEngine.SimilarRatingsLen(SearchEngine.root)
# SearchEngine.preOrderTraversal(SearchEngine.root)
# SearchEngine.Search(SearchEngine.root,1.0,'')
