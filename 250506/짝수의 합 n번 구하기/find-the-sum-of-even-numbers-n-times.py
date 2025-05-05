# 테스트 케이스 수 입력
n = int(input())

# 각 테스트 케이스 처리
for i in range(n):
    a, b = map(int, input().split())
    s = 0
    for i in range(a, b + 1):
        if i % 2 == 0:
            s += i # s = s + i
    print(s)