matrix = []  # 2차원 리스트 초기화

# 4줄 입력받아 2차원 리스트 생성
for _ in range(4):
    row = list(map(int, input().split()))
    matrix.append(row)

# 5의 배수 개수 세기
count = 0
for row in matrix:
    for num in row:
        if num % 5 == 0:
            count += 1

print(count)