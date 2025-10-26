class Solution:
    def removeElement(nums: list[int], val: int) -> int:
        print("")
        i=0
        j=len(nums)-1

        totalFreq=0

        while i<j:
            if nums[i]==val and nums[j]==val:
                j-=1
                totalFreq+=1
                continue
            elif nums[i]==val:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                totalFreq+=1
                j-=1
                i+=1
            elif nums[j]==val:
                totalFreq+=1
                j-=1
            else:
                i+=1
        
        return len(nums)-totalFreq
    
    print(removeElement([3,2,2,3],3))