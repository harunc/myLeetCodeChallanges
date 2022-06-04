class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        if set(s)!=set(t):
            return False
        hashset={}
        for i in s:
            if i not in hashset:
                hashset[i]=1
            else:
                hashset[i]+=1
        hashset1={}
        for i in t:
            if i not in hashset1:
                hashset1[i]=1
            else:
                hashset1[i]+=1
        if hashset1==hashset:
            return True
        else:
            return False

##############################
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        if set(s)!=set(t):
            return False
        countS,countT={},{}
        for i in range(len(s)):
            countS[s[i]]=1+countS.get(s[i],0)
            countT[t[i]]=1+countT.get(t[i],0)
        return countS==countT