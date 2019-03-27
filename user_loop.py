# CLI program for pointlessly asking the user if they want to continue

loop_counter = 0
while(True):
    print("looped: "+ str(loop_counter))
    loop_counter += 1
    user_input = input("Should we continue? ")
    if user_input == "yes":
        continue
    elif user_input == "no":
        print("Thank you for playing!")
        break
    else:
        print("Dont know what you meant, am going to continue to ask!")