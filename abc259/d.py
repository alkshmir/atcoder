import math

# 2円が接するかどうかを返す
def sessuru(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    # 外接
    if d == r1 + r2:
        return True
    elif math.abs(r1 - r2) < d < r1 + r2:
        return True
    elif d == math.abs(r1 - r2):
        return True
    
    return False

