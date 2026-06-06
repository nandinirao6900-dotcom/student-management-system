FILE_NAME = "student.txt"
while True:
    print("---WELCOME TO STUDENT MANAGEMENT SYSTEM---")
    print("1. Add a student")
    print("2. View all students")
    print("3. Search a student")
    print("4. Delete a student")
    print("5. Exit")    
    choice = int(input("ENTER YOUR CHOICE(1,2,3,4,5) = "))
    if (choice == 1):
        name = input("enter the student name = ")
        with open(FILE_NAME, "a") as f :
            f.write(name + "\n")
            print("student added successfully!!!")
    elif(choice == 2):
        try:#used for error handling if file is not found or empty
          with open(FILE_NAME, "r") as f:
            students = f.readlines()
            if (len(students)) == 0 :
               print("no students found !!!")
            else:
               print("the students are :")
               for i,student in enumerate(students , start = 1):
                  print(i, student.strip()) 
        except FileNotFoundError:#handles the error when file is not found
            print("no students found !!!")
    elif(choice == 3):
        name = input("enter the name you want to search = ")
        try:
            with open(FILE_NAME , "r") as f:
                students = f.readlines()#reads all lines from the file and stores them in a list
                found = False #used to track whether the student is found or not
                for student in students:
                    if student.strip() == name:#strip() is used to remove any leading or trailing whitespace characters from the student name
                        found = True#if the student name matches the input name, found is set to True

                        break
                if found:#if found is True, it means the student name was found in the file
                    print("student name is found !!!")
                else:
                    print("student name is not found !!!")

        except FileNotFoundError:
            print("no students found !!!")           
    elif(choice == 4):
            name = input("enter the name of the student you want to delete = ")
            try:
                with open(FILE_NAME , "r") as f:#opens the file in read mode to read the existing student names
                    students = f.readlines()
                with open(FILE_NAME , "w") as f:
                    for student in students:
                        if (student.strip() != name):#if the student name does not match the input name, it is written back to the file. This effectively deletes the student name from the file if it matches.
                            f.write(student)
                print("student deleted successfully !!!")
            except FileNotFoundError:
                print("no students found !!!")
    elif(choice == 5):
        print("THANK YOU FOR USING THE STUDENT MANAGEMENT SYSTEM !!!")
        break
    else:
        print("invalid choice !!!")
