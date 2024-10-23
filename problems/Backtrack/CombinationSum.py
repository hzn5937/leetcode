def combination_sum(candidates, target):
    res = []

    def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return
        elif i >= len(candidates) or total > target:
            return

        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        cur.pop()
        dfs(i+1, cur, total)


    dfs(0, [], 0)

    return res



# print(combination_sum([2, 3, 6, 7], 7))
print(combination_sum([8,7,4,3], 11))