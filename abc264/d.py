
    
s = input()

char_int_map = {
    'a': 1,
    't': 2,
    'c': 3,
    'o': 4,
    'd': 5,
    'e': 6,
    'r': 7
}

seq = [char_int_map[c] for c in s]


def swap(i):
    tmp = seq[i+1]
    seq[i+1] = seq[i]
    seq[i] = tmp

#print(seq)
cnt = 0
while seq != [1,2,3,4,5,6,7]:
    for i in range(6):
        if seq[i] > seq[i+1]:
            swap(i)
            cnt += 1
print(cnt)