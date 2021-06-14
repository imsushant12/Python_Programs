'''
Problem Statement:-
------------------
Take age or year of birth as an input from the user. Store the input in one variable.
Your program should detect whether the entered input is age or year of birth and tell
the user when they will turn 100 years old and age in any desired year.
'''

year_or_age = int(input("Enter your age or year of birth : "))

if(year_or_age < 100):
    age_to_hit_100 = 100 - year_or_age
    print("You will turn 100 at ", 2021 + age_to_hit_100)

else:
    age_to_hit_100 = 100 - (2021 - year_or_age)
    print("You will turn 100 at ", 2021 + age_to_hit_100)

choice = input("Press YES to find age at desired year else type NO : ").lower()

if(choice == "yes"):
    year = int(input("Enter desired year : "))
    if (year_or_age < 100):
        current_age = 2021 - year_or_age
        desired_age = year - current_age
        print("You will be ", desired_age , "in the year " , year)
    else:
        current_age = year - year_or_age
        print("You will be ", current_age , "in the year " , year)
else:
    exit(0)




