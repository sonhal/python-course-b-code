
# CLI program for getting main ingredients for a meal

meal_1 = "meatballs"
main_i_1 = "beef"

meal_2 = "Sushi"
main_i_2 = "salmon"

meal_3 = "Caesar salad"
main_i_3 = "Chicken"

user_meal = input("1: " + meal_1 + ", 2: " + meal_2 + ", 3: " + meal_3 + " ")

if user_meal == 1:
    print(main_i_1)
elif user_meal == 2:
    print(main_i_2)
elif user_meal == 3:
    print(main_i_3)
else:
    print("Dont know what you did there!")