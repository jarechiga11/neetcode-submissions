class Solution:
    def isValid(self, s: str) -> bool:
        # use List as stack, insert any openings to be popped later
        stack = []

        # loop thru string, if opening, add to stack, if closing, pop stack and compare same type
        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
            elif len(stack) < 1:
                return False
            elif self.sameType(stack.pop(), ch) == False:
                return False
        
        # stack should be empty if all openings had closings
        return len(stack) == 0

    def sameType(self, c1, c2):
        if c1 == '(':
            return c2 == ')'
        if c1 == '{':
            return c2 == '}'
        if c1 == '[':
            return c2 == ']'