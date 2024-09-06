print("TICKET MACHINE")

NolCard = input("What is your NolCard? [Y/N]")
multi = input("Is it a family ride? [Y/N] /n")

if (NolCard == "Y"):
    fare = 1.5
elif (multi == "Y"):
    fare = 10
else:
    fare = 4.5

print(fare)
