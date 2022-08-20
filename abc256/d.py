n = int(input())
logs = []
for _ in range(n):
    l, r = [int(s) for s in input().split()]
    logs.append({'time':l, "type":0})
    logs.append({'time':r, "type":1})

sorted_logs = sorted(
  logs,
  key = lambda x: (x['time'], x['type'])
)

#print(sorted_logs)
users = 0 # number of users logged in
for log in sorted_logs:
    if log['type'] == 0: # login
        if users == 0:
            print("{} ".format(log['time']), end='')
        users += 1
        
    else: # logout
        users -= 1
        if users == 0:
            print(log['time'])
    