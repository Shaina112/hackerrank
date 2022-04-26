M = int(input())
m = set(map(int,input().split()))
N = int(input())
n = set(map(int,input().split()))

a = sorted(m^n)

for i in a:
    print(i)