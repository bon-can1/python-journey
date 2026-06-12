a = 12     #  stored a integer 
print(type(a)) # it  will show the type of the var

# print("hello " + a) # it will show an error of TypeError: str and operate with int
# comment the above line and run again

b = str(a) # interger a is changed to string by using "str()"
print(type(b))
print("hello " + b)