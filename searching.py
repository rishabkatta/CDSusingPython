__author__ = 'zjb'

def search(data, val):
    for item in data:
        if item == val:
            return True
    return False

def where(data,val):
    for ind in range(len(data)):
        if data[ind] == val:
            return ind
    return -1

def binsearch(data,val,left,right):
    if left > right:
        return -1
    midindex = (left+right)//2
    if data[midindex] == val:
        return midindex
    if data[midindex] > val:
        return binsearch(data,val,left,midindex-1)
    else:
        return binsearch(data,val,midindex+1,right)

def binary_search(data,val):
    return binsearch(data,val,0,len(data)-1)

nums = [4, 7, 2, 1, 8, 3, 6]
print("5?", search(nums,5))
print("1?", search(nums,1))
print("5?", where(nums,5))
print("1?", where(nums,1))
# binary search on unsorted data
print("binary 1?", binsearch(nums,1,0,len(nums)-1))
# using the helper function
print("binary 1?", binary_search(nums,1)) # why does this work?
print("binary 2?", binary_search(nums,2))
sortednums = [2, 4, 5, 6, 8, 11, 12, 14]
print("binary 2?", binary_search(sortednums,2))
print("binary 7?", binary_search(sortednums,7))