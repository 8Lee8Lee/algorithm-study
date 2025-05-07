# 첫 줄: 행과 열의 개수
n, m = map(int, input().split())

# 첫 번째 격자 입력 받기
grid1 = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid1.append(row)

# 두 번째 격자 입력 받기
grid2 = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid2.append(row)

# 두 격자 비교하여 결과 출력
for i in range(n):
    for j in range(m):
        if grid1[i][j] == grid2[i][j]:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()