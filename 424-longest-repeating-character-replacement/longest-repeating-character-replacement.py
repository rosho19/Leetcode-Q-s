class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 # left pointer
        maxfreq = 0 # keeps track of the frequency of the most frequent character
        maxlen = 0 # keeps track of the longest substring after  up to k replacements
        freq = {} # hashmap of each character and its frequency

        for r in range(len(s)): # runs a right pointer along the input string
            freq[s[r]] = 1 + freq.get(s[r], 0) # increments the current characters' count by 1, insures if it is new it starts with 0
            maxfreq = max(maxfreq, freq[s[r]]) # checks to see if the current character at the right pointer has more than the current most frequent character in the window
            while (r - l + 1) - maxfreq > k: # runs a loop to remove characters from the left pointer until less than k replacements are needed
                freq[s[l]] -= 1
                l += 1

            maxlen = max(maxlen, r - l + 1) # checks if the current substring within the window has longer length than current max length
            r += 1    
        
        return maxlen # returns highest substring length found