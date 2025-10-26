class Solution:
    def intToRoman(num: int) -> str:
        import math
        romanTable={
            1:"I",
            5:"V",
            10:"X",
            50:"L",
            100:"C",
            500:"D",
            1000:"M",
        }
        i=num
        reversed=[]
        while i>=1:
            lastDigit =  math.floor(i%10)
            reversed.append(lastDigit)
            i=i/10
        
        right = len(reversed)-1
        romanAnswer=""
        keys = sorted(romanTable.keys(),reverse=True)
        while right>=0:
            normalDigit = reversed[right]
            digit=int(str(reversed[right]) + "0" * len(reversed[:right]))
            if digit in romanTable:
                romanAnswer+=romanTable[digit]
            else:
                for index,value in enumerate(keys):
                    if digit > value:
                        if normalDigit == 4:
                            romanAnswer+=romanTable[value]+romanTable[keys[index-1]]
                            break
                        elif normalDigit == 9:
                            romanAnswer+=romanTable[keys[index+1]]+romanTable[keys[index-1]]
                            break
                        elif normalDigit>=1 and normalDigit<4:
                            for x in range(normalDigit):
                                romanAnswer+=romanTable[value]
                            break
                        elif normalDigit>5 and normalDigit<9:
                            romanAnswer+=romanTable[value]
                            newDigit = normalDigit-5
                            for x in range(newDigit):
                                romanAnswer+=romanTable[keys[index+1]]
                            break

            right-=1
        return romanAnswer
    
    print(intToRoman(1))