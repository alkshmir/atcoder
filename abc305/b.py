dist = [3, 1, 4, 1, 5, 9]
cul_sum = [0, 3, 4, 8, 9, 14, 23]
dic = {
    'A': 0,
    'B': 1, 
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6
}

p, q = input().split()
p_idx = dic[p]
q_idx = dic[q]
print(cul_sum[max(p_idx, q_idx)] - cul_sum[min(p_idx, q_idx)])