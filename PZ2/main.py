num = int(input())
n1 = (num % 10) * 100
n2 = (num % 100) - (num % 10)
n3 = (num // 100)
print(n1 + n2 + n3)