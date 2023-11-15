user_input = float(input("Enter the mark: "))
if 0 <= user_input <= 100:
    if user_input >= 80:
        grade = 'A+'
    elif user_input >= 75:
        grade = 'A'
    elif user_input >= 70:
        grade = 'A-'
    elif user_input >= 65:
        grade = 'B+'
    elif user_input >= 60:
        grade = 'B'
    elif user_input >= 55:
        grade = 'B-'
    elif user_input >= 50:
        grade = 'C'
    elif user_input >= 40:
        grade = 'D'
    else:
        grade = 'Fail'

    print(f"The grade for the mark {user_input} is: {grade}")
else:
    print("Invalid mark. Please enter a mark between 0 and 100.")
