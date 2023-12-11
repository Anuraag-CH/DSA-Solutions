class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def MAH(arr):
            if len(arr) == 1:
                return arr[0]

            stack = []
            min_element_index_right = []
            for i in range(len(arr) - 1, -1, -1):
                while stack and stack[-1][0] >= arr[i]:
                    stack.pop()

                if stack:
                    min_element_index_right.append(stack[-1][1])

                else:
                    min_element_index_right.append(len(arr))

                stack.append((arr[i], i))

            min_element_index_right.reverse()

            while stack:
                stack.pop()

            min_element_index_left = []

            for i in range(0, len(arr)):
                while stack and stack[-1][0] >= arr[i]:
                    stack.pop()

                if stack:
                    min_element_index_left.append(stack[-1][1])

                else:
                    min_element_index_left.append(-1)

                stack.append((arr[i], i))

            res = 0

            for i in range(0, len(arr)):
                area = (
                    min_element_index_right[i] - min_element_index_left[i] - 1
                ) * arr[i]
                res = max(res, area)

            return res

        rows = len(matrix)
        columns = len(matrix[0])

        cumulative_value_row = [0] * columns

        max_area = 0
        for row in matrix:
            for i in range(columns):
                if int(row[i]) == 0:
                    cumulative_value_row[i] = 0
                else:
                    cumulative_value_row[i] += int(row[i])

            area = MAH(cumulative_value_row)

            max_area = max(max_area, area)
        return max_area
