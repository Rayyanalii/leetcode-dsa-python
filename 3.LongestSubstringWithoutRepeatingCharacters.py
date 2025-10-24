class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        print("")
        freq=set()

        i=0
        j=0
        max=0
        while i < len(s) and j<len(s):
            if i==j:
                if (j-i+1)>max:
                    max=(j-i+1)
                freq.add(s[j])
                j+=1
                continue
            if s[j] not in freq:
                if (j-i+1)>max:
                    max=(j-i+1)
                freq.add(s[j])
                j+=1
            else:
                while s[j] in freq:
                    freq.remove(s[i])
                    i += 1

                freq.add(s[j])
                j+=1
                    
        return max
    
    print(lengthOfLongestSubstring("abcabcbb"))