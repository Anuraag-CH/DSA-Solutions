def permutations(input,output):
    if len(input)==0:
        print(output)
        return

    if input[0].isdigit():
        op1 = output + input[0]
        permutations(input[1:],op1)
    else:
        op1 = output + input[0].lower()
        op2 = output + input[0].upper()
        permutations(input[1:],op1)
        permutations(input[1:],op2)


permutations("a1B2Vfewjf","")