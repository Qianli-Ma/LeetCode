class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketDict = {'(': ')', '[': ']', '{': '}'}
        keys = ['(', '[', '{', " "]
        for char in s:
            if char in keys:
                if char != " ":
                    stack.append(bracketDict[char])
            else:
                try:
                    if char == stack.pop():
                        pass
                    else:
                        return False
                except:
                    return False
        if len(stack) > 0:
            return False
        return True


if __name__ == "__main__":
    # solution = Solution
    a = "["
    print(Solution().isValid(s=a))
