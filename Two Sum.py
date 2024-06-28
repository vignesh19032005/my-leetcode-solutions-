#Difficulty Easy -- 1.Two Sum

class Solution:
    def twoSum(self,nums,target):
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if i!=j:
                    if nums[i]+nums[j]==target:
                        return [i,j]
            
nums = [2,7,11,15]
target=9
s=Solution()
print(s.twoSum(nums,target))
