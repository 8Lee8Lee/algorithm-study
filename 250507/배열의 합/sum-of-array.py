matrix = []  # 2차원 리스트 초기화

# 4줄 입력받아서 2차원 리스트에 저장
for _ in range(4):
    row = list(map(int, input().split()))  # 입력값을 int로 변환한 리스트
    matrix.append(row)  # 한 줄씩 추가

# 각 행의 합 출력
for row in matrix:
    print(sum(row))