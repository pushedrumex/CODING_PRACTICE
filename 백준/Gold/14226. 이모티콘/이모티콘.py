from collections import deque,defaultdict

S = int(input())
visited = defaultdict(bool) # key = (현재, 보드)
q = deque([(1,0,0)]) # 현재, 보드, 시간

while q:
    a = q.popleft()
    if a[0] == S:print(a[2]);break
    if visited[(a[0],a[1])]:continue

    q.append((a[0]-1,a[1],a[2]+1)) # -1
    if a[1]:q.append((a[0]+a[1],a[1],a[2]+1)) # 붙여넣기
    q.append((a[0],a[0],a[2]+1)) # 복사
    
    visited[(a[0],a[1])] = True
