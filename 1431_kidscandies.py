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

        return result
