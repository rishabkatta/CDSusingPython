__author__ = 'zjb'

def ssort(data):
    # k is the number of elements sorted so far
    # thus, k is the index where we will put the next one
   for k in range(len(data)-1):
       minindex = k # initially k'th item is "minimum so far" of remaining elements
       for index in range(k+1,len(data)):
           if data[index] < data[minindex]:
               minindex = index
        # now swap the min value into slot k
       temp = data[k]
       data[k] = data[minindex]
       data[minindex] = temp
       #print(data)
    # no return, data is sorted in-place!

def msort(data):
    if (len(data) == 1):
        return data
    midindex = len(data)//2
    first = msort(data[0:midindex])
    second = msort(data[midindex:len(data)])
    # zip 'em up
    ans = []
    firstind = 0
    secondind = 0
    while firstind < len(first) and secondind < len(second):
        if first[firstind] < second[secondind]:
            ans.append(first[firstind])
            firstind += 1
        else:
            ans.append(second[secondind])
            secondind += 1
    # one array is used up
    if firstind < len(first):
        ans.extend(first[firstind:])
    else:
        ans.extend(second[secondind:])
    return ans



nums = [4, 7, 2, 1, 8, 3, 6]
print(nums)
ssort(nums)
print(nums)
nums = [4, 7, 2, 1, 8, 3, 6]
print(nums)
sortednums = msort(nums)
print(sortednums)