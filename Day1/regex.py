import re

pattern = re.compile(r'[A-Z]')
pattern2 =  re.compile(r'[a-z]')
pattern3 = re.compile(r'[0-9]')
pattern4 = re.compile(r'[^a-zA-Z\s0-9]')
def check_password_strength(str):
  count = 0
  matches = pattern.findall(str)
  if matches:
      count += 1
  
  matches1 = pattern2.findall(str)
  if matches1:
    count=count+1

  matches2 = pattern3.findall(str)
  if matches2:
    count=count+1

  matches3 = pattern4.findall(str)
  if matches3:
    count= count + 1
    
  if(len(str)>6):
    count= count +1
    
  return(count)

str =  str(input("Please enter the password"))
if (check_password_strength(str))<3:
  print("Password is weak")
elif ((check_password_strength(str))>=3 or check_password_strength(str)<4):
      print("Password is strong")
elif (check_password_strength(str))>4:
    print("Password is superstrong")