class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
                continue
            if not stack: 
                return False
            t = stack.pop()
            if c == ')' and t != '(': return False
            elif  c == ']' and t != '[': return False
            elif c == '}' and t != '{': return False
        return False if len(stack) else True
        
		