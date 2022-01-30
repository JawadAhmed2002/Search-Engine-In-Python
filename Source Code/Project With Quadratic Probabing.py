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

IntMovieRatings=[]
for i in movieRatings:
    IntMovieRatings.append(int(float(i)*10))
IntMovieRatings.sort()

class MyHashTable:
    def __init__(self, tableSize):
        self.tableSize = tableSize
        self.hashTable = [0] * self.tableSize
        self.mIdList = [0] * self.tableSize
        self.mVotList = [0] * self.tableSize
        # for i in range(self.tableSize):
        #     self.hashTable[i]=-1
    def Hashing(self, key):
        mod = self.hashTable[key] % self.tableSize
        return mod

    def insert(self, arrayVal,movieIds,movieVot):
        # for i in range(self.tableSize):
        hv=self.Hashing(arrayVal)
        if self.hashTable[hv]==0:
            self.hashTable[hv]=arrayVal
            self.mIdList[hv] = movieIds
            self.mVotList[hv] = movieVot

        else:
            for j in range(self.tableSize):
                newHashVal=(hv+ j**2) % self.tableSize
                if self.hashTable[newHashVal]==0:
                    self.hashTable[newHashVal] = arrayVal
                    self.mIdList[newHashVal] = movieIds
                    self.mVotList[newHashVal] = movieVot
                    break

    def Search(self,lenofdata,key):
        key1 = int(float(key) * 10)
        for i in range(lenofdata):
            # print(self.hashTable[i])
            if self.hashTable[i] == key1:
                print('Movie Rating Is: ',(self.hashTable[i])/10,
                  'Movie Id Is: ',self.mIdList[i],
                  'Movie Voting Is: ',self.mVotList[i])

    def printArray(self,lenofdata):
        for i in range(lenofdata):
            print('Movie Rating Is: ',(self.hashTable[i])/10,
                  'Movie Id Is: ',self.mIdList[i],
                  'Movie Voting Is: ',self.mVotList[i])
            print()
#
def QuadProbSearchEngineMenu():
    print('Wait For Data To Load In The HashTable:....')
    print()
    lenOfData=(len(movieRatings))//30
    SearchEngine=MyHashTable(lenOfData*2)
    for i in range(lenOfData):
        SearchEngine.insert(IntMovieRatings[i],movieIds[i],movieVotings[i])
    print('Data Loaded in HashTable Successfullly:')
    while True:
        print()
        print('Menu to Perform Operations on Search Engine Based On Quadratic probing:')
        print('a. Most Popular Movies In the Given Data Are: ')
        print('b. Least Popular Movies In the Given Data Are: ')
        print('c: Search Any Movie By Giving Rating: ')
        print('d: Print All Data In The HashTable Based On Quadratic probing: ')
        print('e: Exit The Program: ')
        Command = input('Enter any above alphabet to perform operations: ')
        print()
        if Command == 'a':
            print('Most Popular Movies Are Following:')
            SearchEngine.Search(lenOfData,10.0)
        if Command == 'b':
            print('Least Popular Movies Are Following:')
            SearchEngine.Search(lenOfData,1.0)
        if Command == 'c':
            print('Search any movie by giving rating: ')
            data=float(input('Enter movie rating: '))
            SearchEngine.Search(lenOfData,data)
        if Command == 'd':
            print('All The Data In The Tree Is Following:')
            SearchEngine.printArray(lenOfData)
        if Command == 'e':
            print('Program Exit Successfully')
            return quit()

SearchEngine=QuadProbSearchEngineMenu()


# lenOfData=(len(movieRatings))//50
# SearchEngine=MyHashTable(lenOfData)
# for i in range(lenOfData):
#     SearchEngine.insert(IntMovieRatings[i],movieIds[i],movieVotings[i])
# 
# # SearchEngine.printArray(lenOfData)
# # print(SearchEngine.Hashing(0))
# SearchEngine.Search(lenOfData,5.8)