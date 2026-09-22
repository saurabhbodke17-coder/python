# while loop
# whart is while loop 
# this is one of the loops which can be infinite
# this loop is depends on condition thats why it can eassily become infinite
# if condition is note becoming false in such cases it will be infinite

# i = 0
# while i <=5:
#     print(i)
#     i = i + 1

# condition and updation is very important in while loop

# while True:
#     print()
# this loop will become infinite
# we can use break to break the loop or stop its execution

# Practise
# print tble of number asked by user 
# but if user want to pront table upto 30 multiplier or any multiplier 
# that also we should able to do

table_of = int(input("Enter number whose table you want: "))
multiplier = int(input("Upto what multiplier do you want the table: "))

i = 1
while i <= multiplier: # 8
    print(i * table_of)
    i = i + 1 # --> 9

print("Loop Execution is over ")