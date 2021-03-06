from collections import deque

def change(s): # 올림(#)이 있다면 소문자로 변환 후 반환
    temp = deque(s)
    s = []
    while temp:
        if temp[0] == '#':
            temp.popleft()
            s[-1] = s[-1].lower()
        else:s.append(temp.popleft())
    return "".join(s)

def solution(m, mif):
    answer = ''
    d = []
    m = change(m)
    for i in range(len(mif)):
        temp = mif[i].split(',')
        temp[-1] = change(temp[-1])
        t =  60*(int(temp[1][:2])-int(temp[0][:2])) + int(temp[1][3:5])-int(temp[0][3:5]) # 음악이 나온 시간(단위 : 분)
        temp[-1] = temp[-1]*(t//len(temp[-1])) + temp[-1][:t%len(temp[-1])] # 그 시간동안 흘라나온 모든 악보
        if m in temp[-1]:d.append([t,len(mif)-i,temp[-2]]) # 해당 멜로디가 이 악보에 존재한다면
    if not d:return '(None)'
    d = sorted(d,reverse=True)
    return d[0][-1]
