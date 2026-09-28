class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        l=list(s)

        for i in s:
            a=l.pop(0)
            l.append(a)
            if "".join(l)==goal:
                return True
        return False