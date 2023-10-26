def generate_parentheses(n):
    stack = []
    result = [] 

    def backtrack(open, close):
        if open == close == n:
            result.append("".join(stack))
            return

        if open < n:
            stack.append("(")
            backtrack(open + 1, close)
            stack.pop()

        if close < open:
            stack.append(")")
            backtrack(open, close + 1)
            stack.pop()
    
    backtrack(0,0)
    return result


print(generate_parentheses(1))
print(generate_parentheses(2))
print(generate_parentheses(3))