class Solution:
    def isPalindrome(self, s: str) -> bool:
        oddFound=False
        s=self.lower1(s)
        s=self.clean(s)
        hashMap={}
        for i in range(len(s)):
            hashMap[s[i]]=1+hashMap.get(s[i],0)
        for i in hashMap:
            if(hashMap[i]%2==1):
                if oddFound==True:
                    return False
                else:
                    oddFound=True
        for i in range(len(s)//2):
            if(s[i]==s[(i*-1)-1]):
                continue
            else:
                return False
        return True
    
    def lower1(self,s:str):
        s=s.lower()
        return s
    def clean(self,s:str):
        for c in s:
            if ord(c)<48 or (ord(c)>57 and ord(c)<97) or ord(c)>122:
                s=s.replace(c,"")
        return s

##############
l,r=0, len(s)-1
while l<r:
    while l<r and not self.alphaNum(s[l]):
        l+=1
    while r>1 and not self.alphaNum(s[r]):
        r-=1
    if s[l].lower()!= s[r].lower():
        return False
    l,r = l+1,r-1
return True

def alphaNum(self,c):
    return(ord('A')<=ord(c)<= ord('Z')) or
           ord('a')<=ord(c)<= ord('z') or
           ord('0')<=ord(c)<= ord('9')) 