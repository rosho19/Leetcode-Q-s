class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = list(nums)
        temp.sort()
        cur = temp[0];
        last = temp[-1];
        cur_count = 0;
        last_count = 0;
        two_sum = [0] * 2;
        for i in range(len(temp)):
            if cur + last ==  target:
                break
            elif cur + last < target:
                cur_count += 1;     
                cur = temp[cur_count]
            else:
                last_count += 1;
                last = temp[(-1 * last_count) - 1]

        for i in range(len(nums)):
            if cur == nums[i] and cur != 'done':
                two_sum[0] = i
                cur = 'done'
            elif last == nums[i] and last != 'done':
                two_sum[1] = i
                last = 'done'
        return two_sum
