class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        l=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans=[]
        for i in words:
            s=""
            for j in i:
                s=s+(l[ord(j)-97])
            ans.append(s)
        s=set(ans)
        return len(s)

        
                