# Functions in python 
# to define functions in python we start with def keyword 

# def greet():
#     print("Hello")

# res = greet() # Hello
# print(res) # None

# why none because we are not returning any value we are hust printing 
# and print will display output but not return any value 
# for that we have return keyword

# def greet():
#     print("greeting")
#     return "Good Morning"

# res =greet() # greeting
# print(res) # Good Morning


# def greet(name):
#     return f"hello {name} how are you"

# # res = greet() # TypeError: greet() missing 1 required positional argument: 'name'
# res = greet("Saurabh")
# print(res) # hello Saurabh how are you

# name = input("Enter your name: ")
# res = greet(name)
# print(res) # hello Saurabh how are you
# Enter your name: Sujata
# hello Sujata how are you

# function reduces the number of lines of code 
# repetation of code 

# dataframe 

# import pandas as pd
# df = pd.DataFrame({"name":["A" , "B" , "C" , "D" , "E"] , "marks":[50,60,70,80,90]})

# def extend(x):
#     return x + 10

# df["extended_marks"] = df["marks"].apply(extend)
# print(df)


# def function_with_default_arguments(name = "user"):
#     return f"hello {name} good morning"

# res = function_with_default_arguments()
# print(res) # hello user good morning

# res = function_with_default_arguments("Sujata")
# print(res) # hello Sujata good morning

# # will write down one maths function 
# # return inputs , output

# # whenever you are returning more than 1 value from return then it 
# # will return it as a tuple

def add(a,b):
    res = a + b
    return (a , b) , res

inp , output = add(20 , 30)

print(inp) # (20, 30)
print(output) # 50

data , data1 = 10,20
print(data) # 10
print(data1) # 20