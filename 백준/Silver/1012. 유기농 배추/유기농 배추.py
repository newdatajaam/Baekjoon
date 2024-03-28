test = int(input())
for _ in range(test):
    m, n, k = map(int, input().split())
    maps = []
    cnt = 0
    direction_x = [0,0,1,-1] # 위 아래 오 왼
    direction_y = [1,-1,0,0]

    for _ in range(k):
        a, b = map(int, input().split())
        maps.append([a,b])
    while maps:
        stack = [maps.pop(0)]
        while stack:
            x, y = stack.pop()
            for i in range(4):
                nx = x + direction_x[i]
                ny = y + direction_y[i]
                if 0 <= nx < m and 0 <= ny < n and [nx, ny] in maps:
                    stack.append([nx, ny])
                    maps.remove([nx, ny])
        cnt += 1
    print(cnt)