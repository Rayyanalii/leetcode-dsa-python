class Solution:
    def maxArea(height: list[int]) -> int:
        print("")
        i=0
        j=len(height)-1
        max=0

        while i!=j:
            minimum=min(height[i],height[j])
            ans=(j-i)*minimum
            
            if ans > max:
                max=ans
            else:
                if minimum == height[i]:
                    i+=1
                else:
                    j-=1
        return max

    print(maxArea([1,1]))