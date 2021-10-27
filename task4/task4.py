with open('file.txt', 'r') as f1:
    a = (list(map(int, f1.read().split('\n'))))
m = sorted(a)[len(a) // 2]
print(sum(abs(v - m) for v in a))
