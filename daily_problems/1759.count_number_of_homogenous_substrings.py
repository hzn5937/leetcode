def countHomogenous(s: str) -> int:
    res = 0
    count = 1
    prev = s[0]
    for i in range(1,len(s)):
        c = s[i]
        if c == prev:
            count += 1
        if c != prev:
            res += sum(range(1,count+1))
            prev = c
            count = 1
    res += sum(range(1,count+1))
    return res % (pow(10, 9) + 7)