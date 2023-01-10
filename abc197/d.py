# 重心が(x0, y0)と(x_{N/2}, y_{N/2})の中点であり、
# そこから360/N度(2pi/N rad)反時計回りに回転させれば良い
# 回転行列かければできるよね(これ本当に緑？)
# まあ確かに線形代数やってなければ全くわからんかも
import numpy as np
N = int(input())
x0, y0 = [int(s) for s in input().split()]
xn2, yn2 = [int(s) for s in input().split()]
d0 = np.array([x0, y0])
center = np.array([(x0 + xn2)/2, (y0 + yn2)/2])
theta = 2*np.pi/N
rotation = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
ans = rotation @ (d0-center).T + center.T
print(ans[0], ans[1])