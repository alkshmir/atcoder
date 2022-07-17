import numpy as np
N, K = [int(s) for s in input().split()]
P = [int(s) for s in input().split()]

ba = []
eaten_turn = [-1 for _ in range(N)]

for turn in range(N):
    X = P[turn]
    #print("turn: {}, ba:{} X:{}".format(turn, ba, X))
    if len(ba) == 0:
        ba.append([X])
    else:
        bani_mieteiru_cards = np.array([yama[-1] for yama in ba])
        #print(bani_mieteiru_cards)
        # 場に見えている表向きのカードであって書かれた整数が X 以上であるもののうち、
        tmp = bani_mieteiru_cards[bani_mieteiru_cards>=X]
        if len(tmp) == 0:
            ba.append([X])
        else:
            # 書かれた整数が最小のもの
            m = np.min(tmp) 
            #print("m: ", m)
            for i, c in enumerate(bani_mieteiru_cards):
                if c == m:
                    # 引いたカードを表向きで重ねる
                    ba[i].append(X)
                    break

    # その後、表向きのカードが K 枚重ねられた山が場にあればその山のカードを全て食べる
    for i, yama in enumerate(ba):
        if len(yama) == K:
            for cards in ba[i]:
                eaten_turn[cards-1] = turn + 1
            del ba[i]

for e in eaten_turn:
    print(e)
