# https://leetcode.com/problems/arranging-coins


class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Initialize pointers for binary search
        l = 1
        r = n

        # Variable to store the maximum number of complete rows
        rows_possible = 0

        # Binary search loop
        while l <= r:
            # Calculate the midpoint
            mid = (l + r) // 2

            # Calculate the coins needed for the current number of rows
            coins_needed = ((mid) * (mid + 1)) / 2

            # Adjust the search space based on the coins needed
            if coins_needed <= n:
                l = mid + 1
                # Update the possible number of rows if coins needed is less than or equal to the given coins
                rows_possible = mid
            else:
                r = mid - 1
                # Narrow down the search space

        # Return the maximum number of complete rows found
        return rows_possible

