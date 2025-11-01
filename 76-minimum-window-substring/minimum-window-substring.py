class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": # base case where input t string is empty, so we return empty string
            return ""
        freqt, freqw = {}, {} # create two hashmaps to store frequencies of characters from T and from our window

        for c in t: # a loop that iterates through t, incrementing counts of characters in the hashmap with a default value 0
            freqt[c] = 1 + freqt.get(c, 0)

        have, need = 0, len(freqt) # sets up a have and need variable to tell how many of our character requirements we have met for a substring of t in s
        result, length = [-1, -1], 100001 # sets up default values for the result substring indices and it's length

        l = 0
        for r in range(len(s)): # runs a dynamically sized sliding window using two pointers across s
            c = s[r]
            freqw[c] = 1 + freqw.get(c, 0) # increments the hashmap for the frequency of characters in the window

            if c in freqt and freqw[c] == freqt[c]: # if it is a character in t and the frequencies of both hashmaps match, then increment have
                have += 1

            while have == need: # for a substring that is valid, so we have all characters of t, we try to remove extra characters to find shortest substring
                if(r - l + 1) < length: # if the current substring is shorter than our current shortest, we update result values
                    result = [l, r]
                    length = (r - l + 1)
                freqw[s[l]] -= 1 # decrements from window hashmap
                if s[l] in freqt and freqw[s[l]] < freqt[s[l]]: # checks if now the decremented character caused our substring to become invalid
                    have -= 1
                l += 1 # increment left pointer as we shorten substring

        l, r = result # at the end of the loop our shortest found substring is given by the result variable
        return s[l : r + 1] if length != 100001 else "" # return the values between the known indicies if the length has changed from default value(a valid substring was found) otherwise return empty string
