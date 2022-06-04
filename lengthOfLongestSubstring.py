class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setS=set(s)
        a=len(setS)
        c=0
        if(len(s)==0):
            return 0
        while c<len(s):
            if a+c>len(s):
                a=a-1
                c=0
            if len(set((s[c:a+c])))==a:
                return a
            c+=1
        return a

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setS=set()
        l = 0
        res=0
        for r in range(len(s)):
            while s[r] in setS:
                setS.remove(s[l])
                l+=1
            setS.add(s[r])
            res = max(res,r-l+1)
        return res