class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0 # initalize the left pointer and variable to store maxlength of the subarrays we find, and a set to differentiate unique characters
        l = 0
        substr = set()

        for r in range(len(s)): # use iterating variable as right pointer
            while s[r] in substr: # if the value at the right pointer is a duplicate in our set, we increment left pointer and remove the value until it is no longer there
                substr.remove(s[l])
                l += 1
            substr.add(s[r]) # now that the value is either removed or it is new, we can add since it is guaranteed to be unique in the current substring
            maxlen = max(maxlen, r - l + 1) # constantly update our maxlength variable if the current substring is longer 
        return maxlen # return the length of the longest substring