import re
S = input()

if re.search(r'[a-z]', S) is not None and re.search(r'[A-Z]', S) is not None and len(S) == len(set(S)):
    print("Yes")
else:
    print("No")