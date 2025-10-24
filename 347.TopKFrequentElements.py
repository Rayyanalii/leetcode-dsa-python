class Solution:
    def topKFrequent(nums: list[int], k: int) -> list[int]:
        import heapq
        h = []
        freq={}

        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
                
        for key,value in freq.items():
            heapq.heappush(h,(-value,key))
        
        result=[]
        for i in range(k):
            key,value = heapq.heappop(h)
            result.append(value)
        return result
    
    
    print(topKFrequent([1,1,1,2,2,3],2))