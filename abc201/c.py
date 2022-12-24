S = input()
cnt = 0
included = []
not_included = []
for i, s in enumerate(S):
    if s == 'o':
        included.append(i)
    if s == 'x':
        not_included.append(i)

for i in range(10000):
    secret = "{:04d}".format(i)
    invalid = False
    for n in included:
        if str(n) not in secret:
            invalid = True
    for n in not_included:
        if str(n) in secret:
            invalid = True
    if invalid:
        continue
    cnt += 1
print(cnt)