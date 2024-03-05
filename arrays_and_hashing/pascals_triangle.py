# https://leetcode.com/problems/pascals-triangle


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        prev_row = [1]

        for i in range(2, numRows + 1):
            cur_row = [1]

            i = 0
            j = 1
            while j < len(prev_row):
                cur_row.append(prev_row[i] + prev_row[j])
                i += 1
                j += 1

            cur_row.append(1)

            res.append(cur_row)

            prev_row = cur_row

        return res


# Time complexity: O(n^2)
# Space complexity: O(n^2)
