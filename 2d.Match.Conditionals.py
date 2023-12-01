name = input ("What's your name")
match name:
    case "Harry" | "Hermoine" | "Ron":
        print ("Gryffindor")
    case _:
        print ("Who?")

##  Match Does not work with Python above 3.1 ##