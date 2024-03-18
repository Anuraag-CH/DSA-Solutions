# https://leetcode.com/problems/can-place-flowers
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        total_flowers_placed = 0

        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return 1 - n >= 0
            else:
                return n == 0

        # first flower

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            total_flowers_placed += 1

        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            total_flowers_placed += 1

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                total_flowers_placed += 1

        return total_flowers_placed - n >= 0
