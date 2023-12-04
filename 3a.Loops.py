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


howmany = input ("How many times")
for l in range (int(howmany)):

    print ("Meow\n")
    howmany = howmany + 1

    # 26.58  loops
