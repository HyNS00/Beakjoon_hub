import sys
input = sys.stdin.readline
d =[0] * 100
d[1] = 1
d[2] = 1

n = int(input())

for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])