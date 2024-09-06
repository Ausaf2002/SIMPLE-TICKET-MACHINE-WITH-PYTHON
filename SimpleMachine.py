print("TICKET MACHINE")

NolCard = input("What is your NolCard? [Y/N]")
multi = input("Is it a family ride? [Y/N] /n")
print("Calculating....\n")
time.sleep(1)

if (NolCard == "Y"):
    fare = 1.5
elif (multi == "Y"):
    fare = 10
else:
    fare = 4.5

print("Your fare is: ", fare)
