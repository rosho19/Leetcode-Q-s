class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 # set boundaries for each halving iteration

        while l <= r: # runs until r and l are equal, aka they have no element between them
            cur = l + ((r - l) // 2) # ensures no overflow during edge cases
            if nums[cur] > target: # updates right pointer to just before the current middle
                r = cur - 1
            elif nums[cur] < target: # updates left pointer to just after the current middle
                l = cur + 1
            else: return cur # returns the current value since it equals the target

        return -1 # loop ends only if target was not found in the input array so return -1