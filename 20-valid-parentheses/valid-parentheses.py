class Solution:
    def isValid(self, s: str) -> bool:
        parenth_stack =[]
        if len(s) % 2 == 1:
            return False
            
        for p in range(len(s)):
            if s[p] =='(':
                parenth_stack.append(')')
            elif s[p] == '[':
                parenth_stack.append(']')
            elif s[p] == '{':
                parenth_stack.append('}')
            elif not bool(parenth_stack) or s[p] != parenth_stack[-1]:
                return False
            else: parenth_stack.pop()

        if not bool(parenth_stack):
            return True
        return False