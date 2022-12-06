import itertools
S = input()
T = input()

for i, (s, t) in enumerate(itertools.zip_longest(S, T)):
    if s != t:
        print(i+1)
        break