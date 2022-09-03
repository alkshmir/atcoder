import itertools
S = input()

col = {
    1: [7],
    2: [4],
    3: [2, 8],
    4: [1, 5],
    5: [3, 9],
    6: [6],
    7: [10]
}
def existsStandingPin(pins):
    for pin in pins:
        if S[pin-1] == '1':
            return True
    return False

def isAllPinsSitting(pins):
    for pin in pins:
        if S[pin-1] != '0':
            return False
    return True
yes = False
if S[0] == '0':
    # i < j holds
    for i, j in itertools.combinations(range(1,8), 2):
        if abs(i-j) == 1:
            continue
        # それぞれの列には、立っているピンが 1 本以上存在する。
        if existsStandingPin(col[i]) and existsStandingPin(col[j]):
            # あいだ
            #print(i, j)
            for k in range(i+1, j):
                if isAllPinsSitting(col[k]):
                    yes = True
                    break

if yes:
    print("Yes")
else:
    print("No")


