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
# print(IntMovieRatings)
# movieData = {}
# for i in range(len(movieIds)):
#     movieData[movieRatings[i]]=movieIds[i], movieVotings[i]
# print(movieData)
# print(movieIds)

class MyHashTable:

    def __init__(self, arrSize):
        self.arrSize = arrSize
        self.Array = [[] for i in range(self.arrSize)]

    def Hashing(self, key):
        mod = key % self.arrSize
        return mod

    def insert(self, Array, keyvalue, value,value1):

        hash_key = self.Hashing(keyvalue)
        Array[hash_key].append(value)
        Array[hash_key].append(value1)

    def Search(self, key):
        mrating=[]
        mId=[]
        mvoting=[]
        col=[]
        for i in range(len(self.Array)):
            for j in range(len(self.Array[i])):
                if i==key:
                    col.append(j)
                    mrating.append(i/10)
                    mvoting.append(self.Array[i][j])
                    mId.append(self.Array[i][j])
                    # print('Movie Rating is:',i/10,'Column Num is:',j,'Movie Id is:',self.Array[i][j], end=' ')
                    # print('\n')
        if mId!=[]:
            fmIds=mId[0::2]
            fmVotings=mvoting[1::2]
            for i in range(len(fmVotings)):
                print('Movie Rating is:',mrating[i],'Column Num is:',col[i],'Movie Id is:',fmIds[i],
                            'Movie Voting is:',fmVotings[i], end=' ')
                print('\n')
        else:
            print('Data Not Founded')

    def SimilarRatingsLen(self):
        Simrating=[]
        mIdAndmVoting = []
        for i in range(len(self.Array)):
            for j in range(len(self.Array[i])):
                Simrating.append(i/10)
                mIdAndmVoting.append(self.Array[i][j])
        print(Simrating)
        print()
        print(mIdAndmVoting)
        return 'Length Of Similar Rating Movie Is: ',len(Simrating)

    def display_hash(self, hashTable):
        for i in range(len(hashTable)):
            print('HashTable Num: ',i, end=" ")
            for j in hashTable[i]:
                print("-->", end=" ")
                print('Movie Ids: ',j, end=" ")

            print('\n')

def sepChainSearchEngineMenu():
    print('Wait For Data To Load In The HashTable:....')
    print()
    SearchEngine=MyHashTable(150)
    for i in range(len(movieRatings)):
        SearchEngine.insert(SearchEngine.Array,IntMovieRatings[i],movieIds[i],movieVotings[i])
    print('Data Loaded in HashTable Successfullly:')
    while True:
        print()
        print('Menu to Perform Operations on Search Engine Based On Separate Chaining:')
        print('a. Most Popular Movies In the Given Data Are: ')
        print('b. Least Popular Movies In the Given Data Are: ')
        print('c. Similar Rating Movies In the Given Data Are: ')
        print('d: Search Any Movie By Giving Rating: ')
        print('e: Print All Data In The HashTable Based On Separate Chaining: ')
        print('f: Exit The Program: ')
        Command = input('Enter any above alphabet to perform operations: ')
        print()
        if Command == 'a':
            print('Most Popular Movies Are Following:')
            SearchEngine.Search(100)
        if Command == 'b':
            print('Least Popular Movies Are Following:')
            SearchEngine.Search(10)
        if Command == 'c':
            print('Length Of Similar Rating Movies Is Following:')
            print(SearchEngine.SimilarRatingsLen())

        if Command == 'd':
            print('Search Any Movie By Giving Rating:')
            rating=float(input('Enter Rating Of Movie To Find: '))
            SearchEngine.Search(rating*10)
        if Command == 'e':
            print('All The Data In The Tree Is Following:')
            SearchEngine.display_hash(SearchEngine.Array)
        if Command == 'f':
            print('Program Exit Successfully')
            return quit()

Search1=sepChainSearchEngineMenu()

# s = MyHashTable(150)
# for i in range(len(movieIds)):
#     s.insert(s.Array, IntMovieRatings[i],movieIds[i],movieVotings[i])
#
# (s.Search(100))


