N = int(input())
S = input()
quotes = []
ans = []
for s in S:
    if s == "\"":
        if quotes and quotes[-1] == "\"":
            quotes.pop()
        else:
            quotes.append("\"")
    if s == ",":
        if quotes and quotes[-1] == "\"":
            ans.append(s)
        else:
            ans.append(".")
    else:
        ans.append(s)
print(''.join(ans))