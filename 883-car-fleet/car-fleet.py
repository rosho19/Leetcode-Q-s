class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_info = list(zip(position, speed)) # appends the two lists together
        car_info = sorted(car_info, reverse = True) # sorts the car in descending order based on position, speed aligns with the car's position this way
        stack = []
        stack.append(float((target - car_info[0][0]) / car_info[0][1])) # sets base value for stack since there will be at least one fleet

        for i in range(1, len(car_info)): # runs loop starting at 1 since base value is already set
            if float((target - car_info[i][0]) / car_info[i][1]) > stack[-1]: # checks if current cars time is greater than the current slowest time
                stack.append(float((target - car_info[i][0]) / car_info[i][1])) # appends the slower time to stack so we have +1 fleets
        # I am using floats for every calculation just to ensure that there are no errors for calculating after division
        return len(stack)