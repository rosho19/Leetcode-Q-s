class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        rear = len(s) - 1 # set up front and rear pointers

        while front < rear: # run while loop until the pointers either reach the same value, or cross if length of string is odd
            while front < rear and not s[front].isalnum(): # skips past non alphanumeric characters
                front += 1
            while rear > front and not s[rear].isalnum():
                rear -= 1
            if s[front].lower() != s[rear].lower(): # checks if the value doesn't match up. In the case that it's the end of the loop, even if both pointers reach the same value or cross, it should still be false
                return False
            front += 1 # adjusting pointers
            rear -= 1
        return True # returns true since we iterated through the string without any errors, so it is a valid palindrome
