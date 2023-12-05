i = 0
while i != 5:
    print ("meow")
    i = i + 1

# --------

j = 0
while j != 5:
    print ("woof")
    j += 1

# ---------------  lists - square brackets 

for k in [0, 1, 2]:
    print ("Winston is cool - list")

# ---------------- range command

for l in range(4):
    print ("Winston rocks - range")

# range with generic variable

for _ in range(4):
    print ("Winston is cool - generic range\n" )

# ---------------- X it out!

    print ("Winston is cool - multiplied\n" * 3)


# ---------------- user input 


howmany =  int(input("How many times"))
for l in range (int(howmany)):

    print ("Meow\n")
    howmany += 1

    # 26.58  loops

# user input with validation

while True:
    try:
        howmany = int(input("How many times (enter 0 to exit): "))
        if howmany == 0:
            print ("Exiting")
            break
        elif howmany > 0:
            print ("Ok\n" * howmany)
            
        else:
            print("Non negative number please")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# same program defined as a function


def print_ok_times():
    while True:
        try:
            howmany = int(input("How many times (enter 0 to exit): "))
            if howmany == 0:
                print("Exiting the program.")
                break
            elif howmany > 0:
                print("OK\n" * howmany)
                # return keeps the value in memory for later
                return howmany
            else:
                print("Non-negative number please")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Call the function to start the program
print_ok_times()

# return command brings back a value to the user of prg

# 35.09