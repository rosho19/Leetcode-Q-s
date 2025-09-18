class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # defining a hashmap to group anagrams based on their character count, setting it as a list for the intial case

        for i in strs: # iterating through the list to get each string
            letters = 26 * [0] # creating a constant size array to store each possible character count
            for j in i: # i is already the string so we iterate over it
                letters[ord(j) - ord("a")] += 1 # ord gives us the value of the ascii character

            result[tuple(letters)].append(i) # lists cannot be keys in python, so we set as tuple since they are unmutable
        return list(result.values()) # we want a list of sublists