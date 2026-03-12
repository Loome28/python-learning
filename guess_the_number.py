nr = input("Guess a number: ")
while nr != "7":    
    print("Wrong, try again.")
    nr = input("Guess a number: ")
if nr == "7":
    print("Correct!")