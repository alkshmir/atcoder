from collections import defaultdict
S = input()
#alphabets = defaultdict(bool)
alpha = [set()]
stack = []
for i, s in enumerate(S):
    if s == '(':
        #stack.append(i)
        alpha.append(set())
        alpha[-1] = alpha[-1] | alpha[-2]
    elif s == ')':
        #j = stack.pop()
        #print(S[j+1:i])
        #for t in S[j+1:i]:
        #    alphabets[t] = False
        alpha.pop()
    else:
        if s in alpha[-1]:
            #print(i, s, alpha[-1])
            print("No")
            exit()
        alpha[-1].add(s)
    #print(i, alpha)
print("Yes")