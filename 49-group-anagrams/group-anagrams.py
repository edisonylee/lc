class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Given an array of strings strs, group the anagrams together. You can return the answer in any order.
        # So, given random array of strings, group the words that have all the same letters and frequencies together.

        # We can sort all of the strings within the array, strings that are the same can be added to as well.
        dic = {}
        for word in strs:
            key = "".join(sorted(word)) # remember we want to store the sorted word as a key
            if key in dic:
                dic[key].append(word)
            else:
                dic[key] = []
                dic[key].append(word)
        return list(dic.values())