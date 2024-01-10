def permutations(input,output):
    if len(input)==0:
        print(output)
        return

    op1 = output + input[0]
    op2 = output + input[0].upper()
    permutations(input[1:],op1)
    permutations(input[1:],op2)


permutations("abc","")