name='Chimi'
age=13
weight=49.50
isStudent=True

print("data type of name before type casting is", type(name))
print("data type of age before type casting is", type(age))
print("data type of weight before type casting is", type(weight))
print("data type of isStudent before type casting is", type(isStudent))

age=float(age)
weight=int(weight)
isStudent=str(isStudent)

print("data type of age after type casting is",type(age))
print("data type of weight after type casting is",type(weight))
print("data type of isStudent after type casting is",type(isStudent))