class solution:
    def longestConsecuative(self,nums:List[int])->int:
    numset=set(nums)
    longest=0
        for n in nums:
            ###check if its the start of a sequence###
            if(n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length+=1
                longest = max(length,longest)
        return longest
if len(nums)==0:
            return 0
        hashMap={}
        maxInd=0
        for i in nums:
            if (i>maxInd):
                maxInd=i
        for i in range(len(nums)):
            hashMap[nums[i]]=1+hashMap.get(nums[i],0)
        cache=[]
        max1=1
        self.rec(hashMap,max1,maxInd,cache,min(nums))
        return max(cache)
    def rec(self,hashMap:set,max1:int,i:int,cache:List[int],size:int):
        if i<size:
            return
        if i in hashMap:
            if i-1 in hashMap:
                max1+=1
                return self.rec(hashMap,max1,i-1,cache,size)
            else:
                cache.append(max1)
                max1=1
                return self.rec(hashMap,max1,i-2,cache,size)
        else:
            return self.rec(hashMap,max1,i-1,cache,size)
            
        