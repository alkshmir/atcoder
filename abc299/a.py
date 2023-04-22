N = input()
S = input()

for i, s in enumerate(S):
    if s == '*':
        if '|' in S[:i] and '|' in S[i:]:
            print("in")
            break
        else:
            print("out")
            break
