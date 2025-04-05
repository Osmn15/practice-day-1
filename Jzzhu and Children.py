n, m = map(int, input().split())
a = list(map(int, input().split()))

max_rounds = 0
last_child = 0

for i in range(n):
    rounds = (a[i] + m - 1) // m 
    if rounds >= max_rounds:
        max_rounds = rounds
        last_child = i + 1  

print(last_child)
