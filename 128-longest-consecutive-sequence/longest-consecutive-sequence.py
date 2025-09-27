class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest_seq = 0
            
        for i in set_nums:
            if (i - 1) not in set_nums:
               length = 1
               while(i + length) in set_nums: 
                    length += 1
               longest_seq = max(length, longest_seq) 
        return longest_seq
