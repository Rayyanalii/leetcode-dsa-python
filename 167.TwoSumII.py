class Solution:
    def twoSum(numbers: list[int], target: int) -> list[int]:
        print("")
        i = 0
        j = len(numbers)-1

        while i!=j:
            sum=numbers[i] + numbers[j]
            if sum == target:
                return [i+1,j+1] 
            if sum<target:
                i+=1
            elif sum>target:
                j-=1
    
    print(twoSum([2,7,11,15],9))