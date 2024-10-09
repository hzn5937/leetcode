class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        result = 0

        for c in s:
            if c == "(":
                open_count += 1
            else:
                open_count -= 1
                if open_count < 0:
                    open_count = 0
                    result += 1
        return result + open_count