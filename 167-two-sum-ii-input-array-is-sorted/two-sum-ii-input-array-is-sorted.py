class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = 0
        rear = len(numbers) - 1

        for i in range(len(numbers)):
            current = numbers[front] + numbers[rear]
            if current == target:
                return [front + 1, rear + 1]
            elif current > target:
                rear -= 1
            else:
                front += 1