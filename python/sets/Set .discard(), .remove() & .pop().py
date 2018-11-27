N = int(input())
s = set(map(int, input().split()))
m = int(input())
for n in range(m):
    x = input().split(" ")
    command = x[0]
    if command == 'remove':
        s.remove(int(x[1]))
    if command == 'discard':
        s.discard(int(x[1]))
    if command == 'pop':
        s.pop()
print(sum(s))







