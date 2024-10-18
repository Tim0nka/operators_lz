input_data = open('input.txt', 'r')
output_data = open ('output.txt','a')
output_data = open ('output.txt','w')
data = input_data.read()
a = int(data)
k = 0
for i in range(2, a // 2+1):
    if (a % i == 0):
        k = k+1
if (k <= 0):
    output_data.write("Число простое")
else:
    output_data.write("Число не является простым")
input_data.close()
output_data.close()