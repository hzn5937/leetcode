def daily_temperatures(temperatures):
    stack = [] 
    res = [0] * len(temperatures) 
    for i, v in enumerate(temperatures):
        while stack and v > stack[-1][1]:
            stackI, stackV = stack.pop()
            res[stackI] = i - stackI
        stack.append([i, v])
    return res

print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(daily_temperatures([30, 40, 50, 60]))
print(daily_temperatures([30, 60, 90]))
