matrix = []

# 2차원 배열 입력
for _ in range(4):
    row = list(map(int, input().split()))
    matrix.append(row)

# 특정 좌표의 합 계산
total = 0
for i in range(4):
    for j in range(i + 1):  # j는 0부터 i까지 (삼각형 범위)
        total += matrix[i][j]

print(total)