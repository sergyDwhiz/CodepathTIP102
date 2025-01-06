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
            reversed_string = ''.join(reversed(string_x))
            # Compare the reversed string to the original string
            if(string_x == reversed_string):
                return True
            else:
                return False