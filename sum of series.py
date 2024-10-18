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
    n+=1


if Sum - sigma > sigma - (Sum - Decimal(1/Decimal(n) ** 2)):
    n -= 1
n -= 1
print(n)