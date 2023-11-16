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
