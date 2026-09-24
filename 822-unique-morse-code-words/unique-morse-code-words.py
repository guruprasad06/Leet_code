class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        l=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        ans=[]
        for i in words:
            s=""
            for j in i:
                s+=(l[ord(j)-97])
            ans.append(s)
        print(ans)
        a=set(ans)
        return len(a)