# Time complexity: O(n)
# Space complexity: O(n)

def findPair(arr, k):
    hash={}
    for ele in arr:
        if ((k-ele) in hash):
            return True
        else:
            hash[ele]=True
    return False
    
print(findPair([4, 5, 1, -3, 6], k = 11))