__author__ = 'rishab katta'
import sys
from collections import namedtuple
import re

Entry = namedtuple('Entry', ('key', 'value'))

'''
To make sure that the DELETED sentinel does not match
anything we actually want to have in the table, make it
a unique (content-free!) object.
'''


class _delobj: pass


DELETED = Entry(_delobj(), None)


class Hashmap:
    __slots__ = 'table', 'numkeys', 'cap', 'maxload', 'collisions', 'probes', 'hashcoice', 'count'

    def __init__(self, hc, initsz=100, maxload=0.9):
        '''
        Creates an open-addressed hash map of given size and maximum load factor
        :param initsz: Initial size (default 100)
        :param maxload: Max load factor (default 0.7)
        '''
        self.cap = initsz
        self.table = [None for _ in range(self.cap)]
        self.numkeys = 0
        self.maxload = maxload
        self.collisions=0
        self.probes=1
        self.hashcoice =hc
        self.count=0

    def put(self, key, value=None):
        '''
        Adds the given (key,value) to the map, replacing entry with same key if present.
        :param key: Key of new entry
        :param value: Value of new entry
        '''

        try:

            self.count=self.get(key)
            self.probes=1
            value = self.count+1
        except KeyError:
            value=1

        firstDeleted = None  # we have to search through the whole line to to make sure we aren't adding duplicates
        index = self.hash_func(key, self.hashcoice) % self.cap
        collisionflag = False

        while self.table[index] is not None and \
                self.table[index].key != key:
            if self.table[index] == DELETED and firstDeleted == None:
                firstDeleted = index
            index += 1
            if index == len(self.table):
                index = 0
            collisionflag = True
            self.probes += 1
        if (collisionflag):
            self.collisions += 1
        # if we encountered a deleted and we didn't find the key change the key index to the first deleted index
        if firstDeleted != None and (self.table[index] == None or self.table[index].key != key):
            index = firstDeleted
        # otherwise if we haven't found the index then increase the size of the occupied cells
        elif self.table[index] is None:
            self.numkeys += 1

        self.table[index] = Entry(key, value)
        if self.numkeys / self.cap > self.maxload:

            # rehashing
            oldtable = self.table
            # refresh the table
            self.cap *= 2
            self.table = [None for _ in range(self.cap)]
            self.numkeys = 0
            self.collisions=0
            self.probes=1
            # put items in new table
            for entry in oldtable:
                if entry is not None:
                    self.put(entry[0], entry[1])

    def remove(self, key):
        '''
        Remove an item from the table
        :param key: Key of item to remove
        :return: Value of given key
        '''
        index = self.hash_func(key, self.hashcoice) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is not None:
            self.table[index] = DELETED

    def get(self, key):
        '''
        Return the value associated with the given key
        :param key: Key to look up
        :return: Value (or KeyError if key not present)
        '''
        index = self.hash_func(key,self.hashcoice) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == self.cap:
                index = 0
            self.probes +=1
        if self.table[index] is not None:
            return self.table[index].value
        else:
            raise KeyError('Key ' + str(key) + ' not present')

    def contains(self, key):
        '''
        Returns True/False whether key is present in map
        :param key: Key to look up
        :return: Whether key is present (boolean)
        '''
        index = self.hash_func(key, self.hashcoice) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == self.cap:
                index = 0
            self.probes += 1
        return self.table[index] is not None

    def hash_func(self, key, choice):
        '''
        Not using Python's built in hash function here since we want to
        have repeatable testing...
        However it is terrible.
        Assumes keys have a len() though...
        :param key: Key to store
        :return: Hash value for that key
        '''
        # if we want to switch to Python's hash function, uncomment this:
        hash1=0
        g=31
        if choice==1:
            #hash function 1
            for c in key:
                hash1 = g*hash1 + ord(c)
            return hash1
        elif choice==2:
            #hash function 2
            for i,c in enumerate(key):
                hash1 += 139**i*(ord(c))
            return hash1
        elif choice==3:
            #python's default hashfunction
            return hash(key)





def printMap(map):
    '''
    This method prints the string version of the map.
    :param map: map to be printed
    :return:
    '''
    for i in range(map.cap):
        print(str(i) + ": " + str(map.table[i]))


def main():
    '''
    main is used to read from a file, put all words into the hashmap, calculate the max repeating word and print out
    number collisions and probes
    :return:
    '''
    try:
        file = "C:/Users/rishab katta/Documents/memoriesofmylife.txt"
        typeofhash = int(input("enter the type of hash function(1/2/3-inbuilt)"))
        loadfact = float(input("enter load factor"))
        assert 0<loadfact<1
        assert 1<=typeofhash<=3
    except:
        print("incorrect arguments")
        sys.exit(0)
    map = Hashmap(hc=typeofhash, maxload=loadfact)
    listofwords=[]
    listofcounts=[]
    allwords=[]
    with open(file, "r") as f:
        for line in f:
            line=line.strip()
            listofwords=re.split('\W+', line)
            for word in listofwords:
                word.strip()
                word=word.lower()
                if word not in ["", " ", ' ', '']:
                    map.put(word)
                    allwords.append(word)

    for word in allwords:
        listofcounts.append(map.get(word))

    print("highest occurring wordcount :" + str(max(listofcounts)))
    print("highest occurring word      :" + str(allwords[listofcounts.index(max(listofcounts))]))
    print("total number of collisions :"+ str(map.collisions))
    print("total number of probes     :"+ str(map.probes))
    printMap(map)





if __name__ == '__main__':
    main()