class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l=s.split()
        if len(pattern)!=len(l):
            return False
        if len(set(pattern))!=len(set(l)):
            return False
        d={}
        for i in range(len(pattern)):
            if pattern[i] not in d:
                d[pattern[i]]=l[i]
            else:
                if d[pattern[i]]!=l[i]:
                    return False
        print(d)
        return True