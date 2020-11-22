n1 = int(input("enter a number :"))
n2 = int(input("enter a numbr : "))

matches = 0 
while  n1 > 0 and n2 > 0 : 
    if  n1 % 10 == n2 % 10  : 
     matches += 1
    n1 = n1 // 10 
    n2 = n2 // 10 

print(matches)