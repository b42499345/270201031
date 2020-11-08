num_1 = int(input("num_1 : "))
num_2 = int(input("num_2 : "))
num_3 = int(input("num_3 : ")) 

if num_3 > num_2 > num_1 or num_2 > num_3 > num_1 : 
  print (num_1)
elif num_2 > num_1 > num_3 or num_1 > num_2 > num_3 :
  print (num_3)
else :
  print (num_2)