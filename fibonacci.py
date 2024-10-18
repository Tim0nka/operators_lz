N = int(input("Введите число "))
f1 = f2 = 1
print(0 ,f1, f2, end=' ')

i = 2
while i < N:
	f1, f2 = f2, f1 + f2
	print(f2, end=' ')
	i += 1