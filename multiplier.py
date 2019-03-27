# CLI program for multiplying numbers


user_number = input("Please type a number: ")
user_number = int(user_number)

sum = user_number
for i in range(user_number):
    print(sum)
    sum = sum * user_number
print(sum)
