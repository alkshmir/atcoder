S = input()

if 'a' not in S:
    print(-1)
    exit()

for i, c in enumerate(reversed(S)):
    if c == 'a':
        print(len(S)-i)
        exit()
