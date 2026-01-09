class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Given an array of strings strs, group the anagrams together. You can return the answer in any order.
        # So, given random array of strings, group the words that have all the same letters and frequencies together.

        # We can sort all of the strings within the array, strings that are the same can be added to as well.
        
        dic = {} # init hashmap
        for word in strs: #loop through words
            key = "".join(sorted(word)) # create a key, this is going to be the word that is sorted
            # sorted operation does this: transforms "eat" -> ['a', 'e', 't'], so we want to use the "".join to list -> string
            if key not in dic: # we want to check the dictionary
                dic[key] = [] # if it's not in the dictionary, we make an empty list
            dic[key].append(word) # Append the word into the key
        return list(dic.values()) # return a list of all of the values