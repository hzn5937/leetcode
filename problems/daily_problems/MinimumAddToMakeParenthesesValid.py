def minAddToMakeValid(s: str) -> int:
    open_count = 0 # tracks number of close parentheses needed
    result = 0 # tracks number of open parentheses needed

    for c in s:
        if c == "(":
            open_count += 1
        else:
            open_count -= 1
            if open_count < 0: # if there are more close parentheses than open parentheses
                open_count = 0
                result += 1

    return result + open_count

# Explanation: open_count < 0 indicates a new set of parentheses is needed
# Example: "())(" -> We have a balanced close and open parentheses but this is not a valid set of parentheses

print(minAddToMakeValid("())("))  # 1