class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort the array so we can work with a more predictable array
        result = []

        for i in range(len(nums)):

            front, rear, target = i + 1, len(nums) - 1, -(nums[i]) # set all required variables, the two pointers and the third value
            
            if nums[i] > 0: # using the sorted array, if the incrementing left pointer is at a positive value, the other two points will also be positive so no pair is possible
                break

            if i > 0 and target == -nums[i - 1]: # since one iteration with a target value will get all possible pairs to go along, we skip all other identical target values
                continue
            
            
            
            while front < rear: # runs until pointers cross or are equal to each other
                cur = nums[front] + nums[rear]

                if cur < target: # if current pair is less than target, increment left pointer
                    front += 1

                elif cur > target: # opposite for right pointer
                    rear -= 1 
                    
                elif cur == target: # appends if current hits target and increments/decrements pointers
                    result.append([-(target), nums[front], nums[rear]])
                    front += 1
                    rear -= 1
                    while nums[front] == nums[front - 1] and front < rear: # we continue to check for other possible pairs for same target but skip over duplicate pairs
                        front += 1
        return result # return all appended triplets  