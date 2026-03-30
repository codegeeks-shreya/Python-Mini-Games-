

# for i in range(100):
#     random_number = random.randint(1, 100)
#     print(random_number)

name = input("What is your name? ")
print("Hello " + name)
#
#
# for i in range (0,10,2): # start, stop, step
#     i += 1
#     print(i)

# while True:
#     password = input("What is your password? ")
#     if password == "<PASSWORD>":
#         break

password = input("What is your password? ")

no_of_try =1
while no_of_try < 3:
    if (password != "37834"):
        print("Try Again " + name)
        password1 = input("What is your password? ")
        no_of_try += 1
        if no_of_try == 3:
            print("Limit exceeded")
    else:
        print("Welcome " + name)
        break








