# brute force
# Time complexity: O(n²)
# Space complexity: O(1)

def firstRepeatingCharacter(str):
  for i in range(len(str)):
    for j in range(i):
      if str[i] == str[j]:
        return str[i]
  return '\0'
