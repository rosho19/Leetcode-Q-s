class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countfrequency = {}
        kfreq = [[] for i in range(len(nums) + 1)] # making an array to set the elements that have i number of occurrences
        
        for i in nums:
            countfrequency[i] = 1 + countfrequency.get(i, 0) # sets default value for a new input to zero, and increments using previous value
        for j, n in countfrequency.items(): # use j, n as key value pair for the items in the hashmap
            kfreq[n].append(j) # based on the number of occurrences of k, the value of the hashmap, we put it into the kth element of the array with the key as the value
        
        result = [] # new array to get the kth most frequent elements from kfreq
        for i in range(len(kfreq) - 1, 0, -1): # set start, distance and increment of loop
            for n in kfreq[i]: # taking each set of values that are the highest to lowest frequently occurring
                result.append(n) # appending those values to new array
                if len(result) == k: # checks to see when we have the k elements that we require and ends loop
                    return result