input_data = open('input.txt', 'r')
output_data = open ('output.txt','a')
data = input_data.read()
N = int(data) 
f1 = f2 = 1
print(0 ,f1, f2, end=' ')

i = 2
while i < N:
	f1, f2 = f2, f1 + f2
	print(f2, end=' ')
	i += 1
print()