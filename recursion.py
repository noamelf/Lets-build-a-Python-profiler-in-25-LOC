def recur(n):
    if n == 0:
        return
    recur(n - 1)


for i in range(5000):
    recur(700)
