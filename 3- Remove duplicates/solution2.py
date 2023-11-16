# Time complexity: O(nlogn)
# Space complexity: depends on the sorting algorithm

def removeDuplicates(arr):
    if len(arr)==0:
        return []
    arr.sort()
    result=[arr[0]]
    for i in range(1,len(arr)):
        if(arr[i]!=arr[i-1]):
            result.append(arr[i])
    return result