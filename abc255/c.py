

x, a, d, n = [int(s) for s in input().split()]

def binary_search():
    left_idx = 0
    right_idx = n-1
    while abs(right_idx - left_idx) != 1:
        middle_idx = (left_idx + right_idx) // 2
        middle_val = a + d * (middle_idx)
        #print(left_idx, middle_idx, right_idx)
        if middle_val == x:
            break
        if x < middle_val:
            if d >= 0:
                right_idx = middle_idx - 1
            else:
                left_idx = middle_idx + 1
            continue
        if x > middle_val:
            if d >= 0:
                left_idx = middle_idx + 1
            else:
                right_idx = middle_idx - 1
            continue
    return left_idx, middle_idx, right_idx

ans = 0
if d >= 0:
    # X<A
    if x <= a:
        # aが最も近い
        ans = abs(a-x)
    # 最後の数はA+D*(N-1)
    elif x >= a + d*(n-1):
        ans = abs(a + d*(n-1) - x) 
    else:
        #tmp_flag = True
        #for i in range(1, n+1):
        #    flag = (a + d*i < x)
        #    if flag ^ tmp_flag: # XOR
        #        break
        i, j, k = binary_search()
        ans = min(abs(a + d*i - x), abs(a + d*j - x), abs(a + d*k - x))

else:
    # Aが最大値
    if a <= x:
        ans = abs(a-x)
    elif x <= a + d*(n-1):
        ans = abs(a + d*(n-1) - x)
    else:
        #tmp_flag = True
        #for i in range(1, n+1):
        #    flag = (a + d*i > x)
        #    if flag ^ tmp_flag: # XOR
        #        break
        i, j, k = binary_search()
        ans = min(abs(a + d*i - x), abs(a + d*j - x), abs(a + d*k - x))

print(ans)