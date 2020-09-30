again = True

while again:
    mark = int(input("enter your mark: "))

    if mark >= 90:
        grade = 'A+'

    elif mark >= 75:
        grade = 'A'

    elif mark >= 60:
        grade = 'B'

    elif mark >= 50:
      grade = 'C'

    else:
        grade = 'F'

    print(f"Your grade is: {grade}")

    another_grade = input("to stop script type 'no' or press enter to continue: ")
    if another_grade == 'no':
        again = False
        print("\ngoodbye!") #\n leaves a line when printing
