# Leetcode Blind 75

## 1071. Greatest Common Divisor of Strings

```
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        return str1[:gcd(len(str1), len(str2))]
```

Solution Implementation

- The `gcdOfStrings()` method starts by checking if the two input strings are equal. If they are, then the GCD is simply the entire string. Otherwise, the method returns an empty string.

- Next, the method defines a recursive function called `gcd()`. This function takes two integers as input and returns their GCD. The function works by repeatedly dividing the larger number by the smaller number until the smaller number is 0. The GCD is then the larger number.

- The `gcdOfStrings()` method then uses the `gcd()` function to calculate the GCD of the lengths of the two input strings. It then returns the first `gcd(len(str1), len(str2))` characters of the first input string.

