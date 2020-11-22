fibonacci_num = int(input("how many fibonacci number : "))
num1 = 0 
num2 = 1 
for i in range(1,fibonacci_num+1) : 
  num3 = num2+num1 
  num1 = num2  
  num2 = num3
print (num1)