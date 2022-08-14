r, c = [int(s) for s in input().split()]

black = True
if r == 1 or r == 15:
    black = True
elif c == 1 or c == 15:
    black = True
elif c == 2 or c == 14:
    black = False
elif r == 2 or r == 14:
    black = False
elif r == 3 or r == 13:
    black = True
elif c == 3 or c == 13:
    black = True
elif c == 4 or c == 12:
    black = False
elif r == 4 or r == 12:
    black = False
elif r == 5 or r == 11:
    black = True
elif c == 5 or c == 11:
    black = True
elif c == 6 or c == 10:
    black = False
elif r == 6 or r == 10:
    black = False
elif r == 7 or r == 9:
    black = True
elif c == 7 or c == 9:
    black = True
else:
    black = False

if black:
    print("black")
else:
    print("white")