from cProfile import run


def run_length_encode(str):
    length = 1
    tmp = str[0]

    lengths = []
    chars = []
    chars.append(str[0])
    for i in range(1, len(str)):
        if str[i] != tmp:
            lengths.append(length)
            chars.append(str[i])
            tmp = str[i]
            length = 1
        else:
            length += 1
    
    lengths.append(length)

    return chars, lengths


S = input()
T = input()

S_chars, S_lengths = run_length_encode(S)
T_chars, T_lengths = run_length_encode(T)

#print(S_chars, S_lengths, T_chars, T_lengths)
if S_chars == T_chars:
    yes = True
    for sl, tl in zip(S_lengths, T_lengths):
        if not (sl == tl or (sl < tl and sl >= 2)):
            yes = False
else:
    yes = False

if yes:
    print("Yes")
else:
    print("No")

