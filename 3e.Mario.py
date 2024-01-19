print("#")
print("#")
print("#")
print ("-------")
for _ in range(3):
    print ("#")
print ("-------")

# function it

def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()

print ("-------  --> make ? mario block" )

def main2():
    print_row(4)

def print_row(width):
    print("?" * width)

main2()

print ("-------  --> make mario block")

def main3():
    print_square(3)

def print_square(size):
    # For each row in square
    for i in range(size): 
            
    # For each brick in row
            for j in range(size):

    # print brick
                print("#", end="")
            print()
main3()

print ("-------  --> make mario block alternate way")

def main4():
    square(3)

def square(size):

    for k in range(size): 
        print ("#" * size)

main4()
