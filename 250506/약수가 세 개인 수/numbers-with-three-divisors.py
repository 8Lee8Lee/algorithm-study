start, end = map(int, input().split())
count = 0

# start부터 end까지 모든 수에 대해 반복
for num in range(start, end + 1):
    divisor_count = 0  # 약수 개수 초기화
    for i in range(1, num + 1):  # 1부터 자기 자신까지 검사
        if num % i == 0:
            divisor_count += 1
    if divisor_count == 3:
        count += 1

print(count)