students = {}
first_time = True

while True:
    if first_time:
        menu = int(input("Welcome to Teacher's journal:\n1 - Add a student\n2 - Add a mark(s)\n3 - See marks\n4 - Calculate average mark\n5 - See whole journal\n6 - Exit"))
        first_time = False
    else:
        menu = int(input('Choose an option: '))
    if menu == 1:
        name = input("Enter student's name: ")
        students[name] = []
        print('The student has been added successfully')
    elif menu == 2:
        name = input("Enter student's name you are writing the marks for: ")
        if name in students:
            mark = list(map(int, input('Enter the marks: ').split()))
            students[name].extend(mark)
            if len(mark) == 1:
                print('The mark has been added succesfully')
            else:
                print('The marks has been added successfully')
        else:
            print('There is no such student in the journal')
    elif menu == 3:
        name = input("Enter student's name whose marks you want to see: ")
        if name in students:
            print(f"{name}'s marks: {students[name]}")
        else:
            print('There is no such student in the journal')
    elif menu == 4:
        name = input("Enter student's name whose average mark you want to calculate: ")
        if name in students:
            if students[name]:
                avg = sum(students[name]) / len(students[name])
                print(f"{name}'s average mark: {avg}")
            else:
                print("This student hasn't got any mark")
        else:
            print('There is no such student in the journal')
    elif menu == 5:
        if students:
            for key, value in students.items():
                print(f"{key}: {value}")
        else:
            print('There are no students in the journal yet')
    elif menu == 6:
        break
