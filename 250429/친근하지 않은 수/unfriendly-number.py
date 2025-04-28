n = int(input())

a = n // 2
b = n // 3
c = n // 5
ab = n // (2*3)
ac = n // (2*5)
bc = n // (3*5)
abc = n // (2*3*5)

result = n - (a + b + c) + (ab + ac + bc) - abc

print(result)