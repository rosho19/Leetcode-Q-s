class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): # base case if s1 is larger than s2, we know that a permutation of s1 cannot fit in s2 so false
            return False

        freq1, freq2 = [0] * 26, [0] * 26 # create two constant space arrays to track the frequency of characters in both strings

        for i in range(len(s1)): # to set up the arrays, we set up s1's array with all its characters, and s2's array with the first s1 size window
             freq1[ord(s1[i]) - ord('a')] += 1
             freq2[ord(s2[i]) - ord('a')] += 1

        matches = 0 # variable to tell how many out of 26 letters are matched between the two arrays
        for i in range(26): # initial check to see the number of matches, this way we don't run this loop again
            matches += (1 if freq1[i] == freq2[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)): # use two pointers to accomodate the window in s2
            if matches == 26: # if the matches reach 26, the window and s1 are permutations
                return True  

            index = ord(s2[r]) - ord('a') # first block where we account for the right pointer, so we add to our window and check for any changes to our matches
            freq2[index] += 1
            if freq1[index] == freq2[index]:
                matches += 1 
            elif freq1[index] + 1 == freq2[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a') # second block where we account for the left pointer, so we remove from our window and check for any changes to our matches
            freq2[index] -= 1
            if freq1[index] == freq2[index]:
                matches += 1 
            elif freq1[index] - 1 == freq2[index]:
                matches -= 1
            l += 1 # increment left pointer 
        return matches == 26 # returns true if the matches are 26 after the loop finishes