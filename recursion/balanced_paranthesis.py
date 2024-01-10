def balanced_paranthesis(output, open, close):
    if open == 0 and close == 0:
        print(output)
        return
    if open != 0:
        balanced_paranthesis(output + "(", open - 1, close)
    if close > open:
        balanced_paranthesis(output + ")", open, close - 1)


if __name__ == "__main__":
    n = int(input())
    balanced_paranthesis("", n, n)