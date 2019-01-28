'''
@author-1:Rishab Katta
@author-2:Akhil karrothu
'''
from instrumented_sort import *
import random
import time
import sys
def generate_data(N):
    '''
    Generate a random sequence of N integers
    :param N: a Non-negative Integer
    :return:
    '''
    listOfNumbers=[]
    for _ in range(N):
        listOfNumbers.append(random.randint(1,N+1000))
    return listOfNumbers

def check_sorted(alist):
    '''

    :param alist: A list containing any number of elements
    :return: True if the list is in sorted fashion, False otherwise
    '''
    for i in range(0,len(alist)-1):
        if(alist[i]<=alist[i+1]):
            continue
        else:
            return False
    return True

def timeandtablegen():
    '''
    This function is used to calculate the time taken by the sorting algorithms and also to generate a table
    consisting of Number of elements in the list, number of comparisons and time taken by the specific algorithm.
    :return: none
    '''
    if(len(sys.argv)>2 or len(sys.argv)<2):
        N=int(input("Please enter the range of numbers"))
    else:
        N = int(sys.argv[1])
    nlist = generate_data(N)
    print("\n")
    print(nlist)
    print("check_sorted before sorting: " + str(check_sorted(nlist)))
    sstarttime = time.time()
    ssortedlist,scount =ssort(nlist)
    stotaltime = (time.time()- sstarttime)
    mstarttime=time.time()
    msortedlist,mcount = msort(nlist)
    mtotaltime=(time.time()-mstarttime)
    print(msortedlist)
    print("check_sorted after sorting: "+ str(check_sorted(msortedlist)))
    print("\n")
    print("ALGORITHM     \t\t N\t    COMPARISONS\t      SECONDS" )
    print("Selection Sort    \t" + str(N)+"\t\t  " + str(scount)+"\t\t\t\t  " + str(stotaltime))
    print("Merge Sort        \t" + str(N) + "\t\t  " + str(mcount) + "\t\t\t\t  " + str(mtotaltime))

timeandtablegen()