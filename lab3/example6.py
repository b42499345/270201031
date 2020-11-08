# a*(x**2)+b*x+c 
a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))
Δ = (b**2) - 4 * a * c 

if  Δ > 0 : 
  print ("there are  a two real roots")
elif  Δ == 0  : 
  print ("there is a one real root")
else : 
  print ("there are two complex roots")
