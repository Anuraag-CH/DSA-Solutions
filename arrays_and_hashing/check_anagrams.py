class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        # edge cases
        # len(1) case

        if len(strs) == 1:
            return [strs]

        # Initialize a dict
        d = {}

        # sort and add to dict the original string
        for i in strs:
            sorted_val = "".join(sorted(i))

            if sorted_val in d:
                d[sorted_val].append(i)
            else:
                d[sorted_val] = [i]

        # return all lists in dict  in the form of list of lists

        res = []

        for i in d:
            res.append(d[i])

        return res
