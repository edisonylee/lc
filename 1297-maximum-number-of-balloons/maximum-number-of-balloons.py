class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        hset = {'b': 0, 'a': 0,'l': 0,'o': 0,'n': 0} # Creating HSet to check if all the characters exist
        for char in text: # loop throgh the text and then you manually count the letters in balloons
            if char in hset:
                hset[char] += 1
    
        least = float('inf') # Sets least to infinity
        for letter, frequency in hset.items(): # loop through the frequency table
            if letter == 'o' or letter == 'l': # 
                frequency //= 2 # rounds down 
            least = min(least,frequency)
        return least