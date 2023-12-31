# Leetcode Blind 75

## 1071. Greatest Common Divisor of Strings

**Solution**
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

## 1431. Kids With the Greatest Number of Candies

**Solution**

```
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        # Create an empty list to store the results
        result = []

        # Loop through the list of candies
        for i in range(len(candies)):
            # If the current candy + extraCandies is greater than or equal to the maximum candy in the list, append True to the result list. Otherwise, append False.

            if candies[i] + extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)
```

```
Example 1:

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
Example 2:

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false]
Explanation: There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
Example 3:

Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]
```

`kidsWithCandies()` This method takes a list of candies and an integer representing the number of extra candies as input and returns a list of booleans, where each boolean indicates whether the corresponding kid can have the greatest number of candies after distributing the extra candies.

The `kidsWithCandies()` method starts by creating an empty list called result to store the results.
It then loops through the list of candies and checks if the current candy + extraCandies is greater than or equal to the maximum candy in the list.

If it is, the method appends True to the result list. Otherwise, the method appends False to the result list.

Finally, the method returns the result list.

# 605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

```
Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
```

```
Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
```

**Solution**

```
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # Add two zeros to the beginning and end of the flowerbed to handle edge cases
        flowerbed = [0] + flowerbed + [0]

        planted = 0
        for i in range(1, len(flowerbed) - 1):
            # If the current plot is empty and both adjacent plots are empty, plant a flower
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                planted += 1

                # If we have planted enough flower, return True
                if planted >= n:
                    return True

        # If we haven't planted enough flowers, return False
        return planted >= n
```

This solution works by iterating through the flowerbed and planting flowers in empty spaces whenever possible. It handles the edge cases by adding two zeros to the beginning and end of the flowerbed. The solution runs in O(n) time, where n is the length of the flowerbed.
