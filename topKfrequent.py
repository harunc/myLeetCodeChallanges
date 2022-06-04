class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        hashset={}
        res=[]
        max1=0
        for i in range(len(nums)):
            hashset[nums[i]]=1+hashset.get(nums[i],0)
        self.rec(res,hashset,k)
        return res
    def rec(self, res:List[int],hashset:set,k:int)->List[int]:
        max1=0
        if hashset=={}:
            return
        flag=0
        for i in hashset:
            if(hashset[i]>max1):
                max1=hashset[i]
                flag=i
        if len(res)==k:
            return
        res.append(flag)
        del hashset[flag]
        print(hashset)
        return self.rec(res,hashset,k)

##########
#MAX HEAP HEAPIFY O(klogn)
import heapq
from collections import defaultdict, Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.using_dict(nums, k)
        #return self.using_heap(nums, k)
    
    def using_dict(self, nums, k):        
        count_dict = defaultdict(int)
        for n in nums:
            count_dict[n]+=1
        return sorted(count_dict, key = count_dict.get , reverse=True)[:k]
    
    
    def using_heap(self, nums, k):        
        count_dict = Counter(nums)
        return heapq.nlargest(k , count_dict , key = count_dict.get)
#BUCKET SORT O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        max_freq = float('-inf')
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
            max_freq = max(max_freq, counter[num])
                
        freq_buckets = [[] for i in range(max_freq)]
        
        for num, freq in counter.items():
            freq_buckets[freq-1].append(num)
            
        ans = []
        i = len(freq_buckets) - 1
        while k > 0 and i >= 0:
            for num in freq_buckets[i]:
                if k <= 0:
                    break
                ans.append(num)
                k -= 1
            i -= 1
            
        return ans

        class Solution:
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        l = []
        for i in nums:
            hash_map[i] = hash_map.get(i, 0) + 1 
        for key, val in hash_map.items():
            l.append([key,val])    
        l.sort(key = lambda x: x[1], reverse=True)
        return [x[0] for x in l[:k]]
