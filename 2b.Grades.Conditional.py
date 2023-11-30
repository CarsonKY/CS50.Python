score = int(input("Score: "))
if score >= 90 and score <= 100:
    print("Grade A")
elif score >= 85 and score <= 90:
    print("Grade B")
elif score >= 75 and score <= 85:
    print("Grade C")
elif score >= 70 and score <= 75:
    print("Grade D")
else:
    print("Grade F")

# Fewer keystrokes

if 90 <= score <=100:
    print("Grade A")
elif 85 <= score <=90:
    print("Grade B")
elif 75 <= score <=85:
    print("Grade C")
elif 70 <= score <=75:
    print("Grade D")
else:
    print("Grade F")

# Even Fewer keystrokes

if score >=90:
    print("Grade A")
elif score >=85:
    print("Grade B")
elif score >=75:
    print("Grade C")
elif score >=70:
    print("Grade D")
else:
    print("Grade F")
