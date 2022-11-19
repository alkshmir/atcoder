H, M = [int(s) for s in input().split()]

while(True):
    uso_h = ((H // 10)*10 + M // 10)
    uso_m = (H % 10)*10 + M % 10
    if (0 <= uso_h <= 23) and (0 <= uso_m <= 59):
        #print(uso_h, uso_m)
        print(H, M)
        break
    
    if M < 59:
        M += 1
    else:
        M = 0
        if H < 23:
            H += 1
        else:
            H = 0
    