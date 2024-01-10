def permutation_spaces(string):
    res = []
    def helper(input, output):
        if len(input)==0:
            res.append(output)
            return
        op1 = output + input[0]
        op2 = output + " " + input[0]
        helper(input[1:], op1)
        helper(input[1:], op2)
    