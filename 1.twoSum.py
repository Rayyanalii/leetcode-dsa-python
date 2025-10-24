class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        seen={}

        for i,x in enumerate(nums):
            newTarget = target-x
            if newTarget in seen:
                return [seen.get(newTarget),i]
            seen[x] = i
    
    print(twoSum([3,2,4], 6))