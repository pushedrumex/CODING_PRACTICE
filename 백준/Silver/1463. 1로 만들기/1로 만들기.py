# 최대한 많이 나눠야 이득

N = int(input())
d = [0]*(N+1)

for i in range(4,N+1):
    d[i] = d[i-1] + 1# 2나 3으로 나누어 떨어지지 않을 경우, -1 불가피
    if i%3 == 0: d[i] = min(d[i//3] + 1,d[i])# 3으로 나누어 떨어지는 경우, 최소 방법
    if i%2 == 0: d[i] = min(d[i//2] + 1,d[i])# 2으로 나누어 떨어지는 경우, 최소 방법
    
print(d[N])
