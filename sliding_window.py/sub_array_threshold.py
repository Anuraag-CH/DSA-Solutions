class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0  # Initialize count of valid subarrays
        i = 0  # Initialize the starting index of the sliding window
        cur_sum = (
            0  # Variable to keep track of the sum of elements in the current window
        )

        # Iterate over the array using a sliding window of size 'k'
        for j in range(len(arr)):
            cur_sum += arr[j]  # Add the current element to the sum of the window

            # Check if the window size has reached 'k'
            if (j - i + 1) == k:
                # If average of current window >= threshold, increment count
                if cur_sum / k >= threshold:
                    count += 1

                # Move the window forward: subtract the element at the start of the window
                cur_sum -= arr[i]
                i += 1  # Increment the starting index of the window

        return count  # Return the total count of valid subarrays
