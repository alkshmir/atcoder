# 数字が9こあるとして、どちらのグループに所属させるかで2**9通り
# 各グループでは、大きい順に上の桁から決めていけばいい。
# ８けたなら、8つの要素ソートすればいいので、ほとんど時間はかからない。

N = int(input())
nums = []
for s in str(N):
    nums.append(int(s))
keta = len(nums)

ans = 0
for i in range(2**keta):
    groups = [[], []]
    for j in range(keta):
        if (i >> j) & 1:
            groups[0].append(nums[j])
        else:
            groups[1].append(nums[j])
    if not groups[0] or not groups[1]:
        continue
    # 各グループでソートして上から選ぶ
    g1 = int(''.join([str(n) for n in sorted(groups[0], reverse=True)]))
    g2 = int(''.join([str(n) for n in sorted(groups[1], reverse=True)]))
    ans = max(ans, g1*g2)
print(ans)