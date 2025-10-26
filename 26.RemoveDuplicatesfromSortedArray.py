class Solution:
    def removeDuplicates(nums: list[int]) -> int:
        print("")
        i=0
        for j in range(len(nums)):
            if i==j:
                continue
            if nums[i] != nums[j]:
                i+=1
                nums[i] = nums[j]
        return i+1
    
    print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))