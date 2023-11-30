# The symbol == means comparing variables are they equal
# The symbol != means not equal to

# Compare program
x = int(input( "What is X? "))
y = int(input( "What is Y? "))

if x < y:
    print("x is less than y")
if x > y:
    print("x is more than y")
if x == y:
    print("x is equal to y")

# else if with just else

if x < y:
    print("x is less than y")
elif x > y:
    print("x is more than y")
else:
    print("x is equal to y")

# or

if x < y or x > y:
    print("x is not equal to y")

else:
    print("x is equal to y")

# using !=

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
