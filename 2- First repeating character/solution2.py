# Time complexity: O(n)
# Space complexity: O(n)

def firstRepeatingCharacter(str):
    hash={}
    for letter in str:
        if(hash.get(letter)):
            return letter
        else:
            hash[letter]=True
    return '\0'