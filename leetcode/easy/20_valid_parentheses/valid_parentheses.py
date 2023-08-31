class Solution:
    pair = {'{': '}', '(': ')', '[': ']'}

    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        for char in s:
            # if the next character is an open bracket it is accepted
            if char in ('(', '{', '['):
                stack.append(char)
            # if the stack is empty and the next character is a close
            # bracket then we know it cannot match
            elif len(stack) == 0:
                return False
            # if we have a close bracket and the previous character is not its
            # matching open bracket then it is invalid
            elif self.pair[stack.pop()] != char:
                return False
        # if we finish parsing and there are still characters on the stack it
        # means that more brackets were opened than closed
        if len(stack) > 0:
            return False
        return True
