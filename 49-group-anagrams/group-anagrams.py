class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Loop through the words in strs
        # 2. Sort the word and that as a key to access the hashmap
        # 3. Append it to the hashmap key as a list
        dic = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in dic:
                dic[key] = []
            dic[key].append(word)
        return list(dic.values())
            
