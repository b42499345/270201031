gpa = float(input("GPA:"))
num_lectures = int(input("number of lectures:"))

if gpa < 2.0 and num_lectures < 47  : 
  print("not enough number of lecutres and GPA")
elif gpa >= 2.0 and num_lectures < 47 : 
  print ("not enough number of lecutres")
elif gpa < 2.0 and num_lectures >= 47 :  
  print("not enough GPA")
else :
  print("GRADUATED!!!")