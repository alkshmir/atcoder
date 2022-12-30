# 数学無理！
import math
N = int(input())
sqrtN = math.isqrt(N)
print(2*sum([N//i for i in range(1, sqrtN+1)]) - sqrtN**2)