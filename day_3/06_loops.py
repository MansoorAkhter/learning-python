# while loop & for loop

# while loop
# x = 0
# while (x <= 5):
#     print(f"Iteration {x}:") #f(formatted)-string same like template literals `${}` of Javascript
#     print(x)
#     x = x + 1
# print("While loop completed")

# for loop
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
counter = 1
for day in days:
    if(day=="Fri"):continue #skip Fri
    print(f"{counter} -- {day}")
    counter+=1