class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        l=list(s)
        for i in s:
            a=l.pop(0)
            l.append(a)
            if "".join(l)==goal:
                return True
        return False
            

'''       a=s+s
        if len(s)==len(goal):
            for i in a:
                if goal in a:
                    return True
                else:
                    return False
        return False
'''
