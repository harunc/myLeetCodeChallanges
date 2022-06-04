class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        prev=-19191919
        for i in range(len(nums)):
            if(nums[i]==prev):
                return True
            prev=nums[i]
        return False