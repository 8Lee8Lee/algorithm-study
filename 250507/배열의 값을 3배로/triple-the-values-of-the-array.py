# 3x3 배열 입력받기
array = [list(map(int, input().split())) for _ in range(3)]

# 각 요소를 3배해서 출력
for row in array:
    print(' '.join(str(x * 3) for x in row))