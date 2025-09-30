class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        token_stack = []
        operand1 = 0
        operand2 = 0

        for i in tokens:
            if i == "+" or i == "-" or i == "*" or i == "/":
                operand2 = int(token_stack.pop())
                operand1 = int(token_stack.pop())
                if i == "+":
                    token_stack.append(operand1 + operand2)
                elif i == "-":                                
                    token_stack.append(operand1 - operand2)
                elif i == "*":              
                    token_stack.append(operand1 * operand2)
                elif i == "/": 
                    token_stack.append(int(operand1 / operand2))
            else: token_stack.append(i)

        return int(token_stack.pop())