# You are given a positive integer n. Each digit of n has a sign according to the following rules:

# The most significant digit is assigned a positive sign.
# Each other digit has an opposite sign to its adjacent digits.
# Return the sum of all digits with their corresponding sign.



# Example 1:

# Input: n = 521
# Output: 4
# Explanation: (+5) + (-2) + (+1) = 4.


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        N=str(n)
        count=0
        for i in range(len(N)):
            if (i+1)%2!=0:
                count+=int(N[i])
            else:
                count-=int(N[i])
        return count