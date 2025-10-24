class Solution:
    def isAnagram(s: str, t: str) -> bool:
        print("")
        SfreqTable={}
        TfreqTable={}
        for char in s:
            SfreqTable[char] = SfreqTable.get(char,0) + 1
        
        for char in t:
            TfreqTable[char] = TfreqTable.get(char,0) + 1
        
        for key,value in SfreqTable.items():
            if TfreqTable.get(key,0) != value:
                return False
            
        return True
    
    print(isAnagram("rat","car"))