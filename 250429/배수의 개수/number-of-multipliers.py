a_cnt = 0
b_cnt = 0

for i in range(10):
    num = int(input())
    if num % 3 == 0:
        a_cnt += 1
    if num % 5 == 0:
        b_cnt += 1

print(a_cnt, b_cnt)