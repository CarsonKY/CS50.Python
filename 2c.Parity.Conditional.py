#x = int(input("Parity check - What is X? "))
#if x % 2 == 0:
#    print("Number is Even")
#else:
#    print("Number is Odd")

# -----------------------------

# is_even user defined

def main():
        x = int(input("Parity check - What is X? "))
        if is_even(x):
                print("Number is Even")
        else:
                print("Number is Odd")





def is_even(n):
        
        if n % 2 ==0:
                return True
        else:
                return False

# Another way to calculate - return True if n % 2 ==0 else False

main()