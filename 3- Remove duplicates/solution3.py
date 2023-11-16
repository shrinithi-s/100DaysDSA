# Time complexity: O(n)
# Space complexity: O(n)

def removeDuplicates(arr):
    result=[]
    hash={}
    for num in arr:
        if(hash.get(num)):
            pass
        else:
            hash[num]=True
            result.append(num)
    return result