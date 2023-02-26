N = int(input())
S = input()

visited = set()
x = 0
y = 0
visited.add((x,y))

for c in S:
    if c == 'R':
        x += 1
    elif c == 'L':
        x -= 1
    elif c == 'U':
        y += 1
    elif c == 'D':
        y -= 1
    if (x, y) in visited:
        print("Yes")
        exit()
    visited.add((x,y))

print("No")