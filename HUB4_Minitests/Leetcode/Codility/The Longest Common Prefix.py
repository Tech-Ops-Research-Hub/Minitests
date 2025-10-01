class Solution: 
    def longestCommonPrefix (self, strs):
         if not strs:
                return ""
         prefix = strs[0]
         for s in strs[1:]:
                while not s.startswith(prefix):
                    prefix = prefix[:-1]
                    if not prefix:
                        return ""
         return prefix   
     
     
     #the class solution contains the method longestCommonPrefix which takes a list of strings as input and returns the longest common prefix among them. If there is no common prefix, it returns an empty string as an input
     #If strings is empty, it returns an empty string
     #It initializes the prefix as the first string in the list and iterates through the remaining strings
     #For each string, it checks if it starts with the current prefix. If not, it shortens the prefix by removing the last character until a match is found or the prefix becomes empty
     #Finally, it returns the longest common prefix found
     #The time complexity of this solution is O(S) where S is the sum of all characters in all strings. In the worst case, we might have to compare each character of each string.
    #The space complexity is O(1) since we are using only a constant amount of extra space.
