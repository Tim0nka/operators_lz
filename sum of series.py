from decimal import Decimal
L = Decimal(input("Введите начальную сумму: "))
E = int(input("Введите количесто знаков после запятой: "))
S = Decimal(input("Введите конечную сумму: "))
Sum = 0
n = 1

sigma = S - L
S = round(S, E)

while Sum < sigma:
    Sum += Decimal(1)/Decimal(n) ** 2
    print(Sum)
    n+=1


if n != 1 and (Sum - Decimal(S) < Decimal(S) - (Sum - Decimal((1/(n-1)**2)))):
    n -= 1
else:
    n = 1
n -= 1
print(n)