class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_of_digits = 0 # init ans
        x_string = str(x) # convert int to str to loop
        for digit in x_string: # loop thru str
            integer_digit = int(digit) # convert chr to int
            sum_of_digits += integer_digit # add to integer
        if x % sum_of_digits == 0: # remainder 
            return sum_of_digits # return sum
        else:
            return -1