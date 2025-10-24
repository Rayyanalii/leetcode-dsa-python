class Solution:
    def containsDuplicate(nums: list[int]) -> bool:
        seen=set()
        for i,val in enumerate(nums):
            if val in seen:
                return True
            seen.add(val)
            
        return False

    print(containsDuplicate(nums=[1,2,3,4]))