def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []  # Stack to store opening brackets

        for char in s:
            if char in "({[":  # If it's an opening bracket, push to stack
                stack.append(char)
            else:  # If it's a closing bracket
                if not stack:  # Stack should not be empty
                    return False
                top = stack.pop()  # Get the last opening bracket
                if (char == ")" and top != "(") or \
                (char == "}" and top != "{") or \
                (char == "]" and top != "["):
                    return False  # If brackets don't match, return False

        return not stack