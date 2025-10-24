class Solution:
    def groupAnagrams(strs: list[str]) -> list[list[str]]:
        print("")
        seen={}
        result:list[list[str]]=[]
        for i,word in enumerate(strs):
            sort="".join(sorted(word))
            if sort not in seen:
                seen[sort] = len(seen)
                result.append([word])
            else:
                old = result[seen[sort]]
                old.append(word)
                result[seen[sort]]=old
        
        return result
    
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))