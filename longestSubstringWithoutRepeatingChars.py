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
                
            