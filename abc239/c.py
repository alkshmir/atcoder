def possible_dots(x, y):
    return [(x-2, y+1), (x-1, y+2), (x+1, y+2), (x+2, y+1), (x+2, y-1), (x+1, y-2), (x-1, y-2), (x-2, y-1)]

x1, y1, x2, y2 = [int(s) for s in input().split()]
c1 = possible_dots(x1, y1)
c2 = possible_dots(x2, y2)
for c in c1:
    if c in c2:
        print("Yes")
        exit()
print("No")