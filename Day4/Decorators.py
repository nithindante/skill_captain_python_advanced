def authorise(my_function):
  def accept_or_not():
      name = input("Enter your name: ")
      arr =["Nikhil","Arun","Nithin"]
      
      if name in arr:
          my_function()
          
      else:
          print("Access Denied")
  return accept_or_not

@authorise
def my_function():
    print("Granted")

my_function()

