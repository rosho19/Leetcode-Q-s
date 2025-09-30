class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        token_stack = []
        operand1 = 0
        operand2 = 0

        for i in tokens:
            if i == "+" or i == "-" or i == "*" or i == "/": # first checks if we have an operator
                operand2 = int(token_stack.pop()) # initializes the operands to the values in the stack
                operand1 = int(token_stack.pop())
                if i == "+": # completes operation based on specific operator
                    token_stack.append(operand1 + operand2) # pushes resulting value back onto stack
                elif i == "-":                                
                    token_stack.append(operand1 - operand2)
                elif i == "*":              
                    token_stack.append(operand1 * operand2)
                elif i == "/": 
                    token_stack.append(int(operand1 / operand2)) # tricky, but this truncates towards 0 both ways
            else: token_stack.append(i)

        return int(token_stack.pop()) # final value should be the result of the expression