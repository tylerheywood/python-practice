# https://leetcode.com/problems/valid-parentheses/
opening = ["(", "{", "["]

def stack_parser(s: str) -> bool:
    s_stack = []

    for char in s:
        if char in opening:
            s_stack.append(char)

        elif char == ")":
            if not s_stack or s_stack[-1] != "(":
                return False
            s_stack.pop()

        elif char == "}":
            if not s_stack or s_stack[-1] != "{":
                return False
            s_stack.pop()

        elif char == "]":
            if not s_stack or s_stack[-1] != "[":
                return False
            s_stack.pop()

        else:
            return False

    return len(s_stack) == 0



print(stack_parser("[]()}"))   # False
print(stack_parser("()[]{}"))  # True
print(stack_parser("(()"))     # False
print(stack_parser("([])"))    # True
print(stack_parser(")("))      # False
