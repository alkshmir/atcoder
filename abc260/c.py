N, X, Y = [int(s) for s in input().split()]

def count_level1blue_from_red(red_level):
    if red_level == 2:
        return X * count_level1blue_from_blue(2)
    if red_level == 1:
        return 0
    return count_level1blue_from_red(red_level-1) + X * count_level1blue_from_blue(red_level)

def count_level1blue_from_blue(blue_level):
    if blue_level == 2:
        return Y
    return count_level1blue_from_red(blue_level-1) + Y * count_level1blue_from_blue(blue_level -1 )

print(count_level1blue_from_red(N))