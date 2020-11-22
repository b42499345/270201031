n = int(input("how many numbers? "))

even_count = 0 
for i in range(n):   
  number = (int(input("enter a integer: ")))
if number % 2 == 0 : 
  even_count += 1 

print ("%", ((even_count / n )  * 100))
 