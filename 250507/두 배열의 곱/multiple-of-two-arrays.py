# 첫 번째 배열 입력 받기
array1 = []
for _ in range(3):
    row = input().split()
    int_row = []
    for value in row:
        int_row.append(int(value))
    array1.append(int_row)

# 두 번째 배열 입력 받기
array2 = []
for _ in range(3):
    row = input().split()
    int_row = []
    for value in row:
        int_row.append(int(value))
    array2.append(int_row)

# 같은 위치의 숫자 곱해서 출력
for i in range(3):
    for j in range(3):
        print(array1[i][j] * array2[i][j], end=' ')
    print()