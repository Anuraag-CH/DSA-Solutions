class Solution:
    def trap(self, height: List[int]) -> int:
        # Check if the list has less than or equal to 2 elements, in which case no water can be trapped.
        if len(height) <= 2:
            return 0

        max_element = -1

        max_element_left = [-1]

        # Calculate the maximum height to the left of each element in the 'height' list.
        for i in range(1, len(height)):
            max_element = max(max_element, height[i - 1])
            if max_element > height[i]:
                max_element_left.append(max_element)
            else:
                max_element_left.append(-1)

        max_element = -1

        max_element_right = [-1]

        # Calculate the maximum height to the right of each element in the 'height' list.
        for i in range(len(height) - 2, -1, -1):
            max_element = max(max_element, height[i + 1])
            if max_element > height[i]:
                max_element_right.append(max_element)
            else:
                max_element_right.append(-1)

        max_element_right.reverse()

        rain_water_stored = 0

        # Calculate the amount of rainwater that can be trapped at each element and sum them up.
        for i in range(0, len(height)):
            val = min(max_element_left[i], max_element_right[i]) - height[i]
            rain_water_stored += val if val > 0 else 0

        return rain_water_stored
