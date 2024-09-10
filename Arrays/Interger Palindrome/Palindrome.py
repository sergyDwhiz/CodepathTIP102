class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # You can't reverse a negative sign
        if(x<0):
            return False
        else:
            # Convert x to a string
            string_x = str(x)
            # Reverse the string
            reversed = string_x[::-1]
            reversed_int = int(reversed)
            if(reversed_int == x):
                return True
            return False