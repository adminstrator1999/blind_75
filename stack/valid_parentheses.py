class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"}": "{", "]": "[", ")": "("}
        for p in s:
            if p not in pairs:
                stack.append(p)
            elif stack and stack[-1] == pairs[p]:
                stack.pop()
            else:
                return False
        return not stack