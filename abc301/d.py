# Tの最大値と最小値は簡単に求まる
# N >= max(T)のときはmax(T)を出力すればいい
# N <  min(T)のときは-1を出力すればいい
# よって、max(T) > N >= min(T)のときをかんがえる
# 上位桁からみていって、?のけたを1にして、ほかの桁は0にする。
# このときNより大きくなる場合はみている桁を0に、
# N以下になる場合は1に決定する
# 最後の?の桁をきめるときにN以下になっているほうを出力する
# 高々60桁なので十分間に合う

S = input()
N = int(input())

max_T = int('0b' + S.replace('?', '1'), 2)
min_T = int('0b' + S.replace('?', '0'), 2)

if N >= max_T:
    print(max_T)
    exit()
if N < min_T:
    print(-1)
    exit()


#print(bin(N))

tmp_S = [s for s in S]
for i in range(len(S)):
    if S[i] != '?':
        continue

    tmp_S[i] = '1'
    tmp_S_value = int('0b' + ''.join(tmp_S).replace('?', '0'), 2)
    if tmp_S_value > N:
        tmp_S[i] = '0'
    else:
        tmp_S[i] = '1'

#print(tmp_S)
print(int('0b' + ''.join(tmp_S), 2))