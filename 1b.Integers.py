#Generic calculator / integer practice

# calc1 = int(input("What is your first num to calculate "))
# calc2 = int(input("What is your first num to calculate "))
# sum1 = int(calc1) + int(calc2)
# print(sum1)
# print (calc1 + calc2)

#Float - Float supports partial numbers

# calc1 = float(input("What is your first num to calculate as a float "))
# calc2 = float(input("What is your first num to calculate as a float "))

# print (calc1 + calc2)

#Rounding

#round(number[, ndigits]) - Rounds a number dropping fractions by default or add fraction with ndigit

calc1 = float(input("What is your first num to calculate and round "))
calc2 = float(input("What is your first num to calculate and round "))
calcround = (round(calc1 + calc2))
print (calcround)

# add a comma seperation for easier reading
calc3 = (calc1 + calc2)
print (f"{calcround:,}")

# add two decimal places with comma
print (f"{calcround:,.2f}")

# Dividing

calcrounddivide = round(calc1 / calc2 ,2)
print (calcrounddivide)

# Dividing with commas and periods in place
print (f"{calcrounddivide:,.2f}")


