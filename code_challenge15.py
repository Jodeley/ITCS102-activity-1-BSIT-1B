import os
import json
os.system('cls')
print("+++++++++++++++++++++++++++++\nSTUDENT'S INFORMATION SYSTEM\n+++++++++++++++++++++++++++++")

#empty dictionary
student_record = {}

while True:
    print("Select from the following options")
    print("A - Add Student Record")
    print("B - Print all Student Record")
    print("C - Search Student Record")
    print("D - Delete Student Record")
    print("E - Edit Student Record")
    print("F - Export Student Record")
    print("G - Import Student Record")
    print("X - System Exit")

    choice = input("Please Select from options above ----> ").lower()

    if choice == 'a':
        os.system('cls')
        print("\nAdding Student Record")
        id_no = input("Please enter your ID number ----> ")
        first_name = input("Please enter your first name ----> ")
        last_name = input("Please enter your last name ----> ")
        age = input("Please enter your age ----> ")
        section = input("Please enter your section ----> ")
        course = input("Please enter your course ----> ").upper()

        student_record[id_no] = [first_name, last_name, age, section, course]
        print("Data saved successfully")
        continue

    elif choice == 'b':
        os.system('cls')
        print("Printing Students Record")

        for a, b in student_record.items():
            print(f"CODE - {a}, INFORMATION - {b}")
        continue
    elif choice == 'c':
        os.system('cls')
        print("Search Student Record")

        search_id = input("Please enter your ID number ----> ").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print("=========================\n\nRecord Found")
                # print the record for search id
                for i in student_record[search_id]:
                    print(f" --- {i}")
                print("=========================")
            else:
                print(f"Sorry, no record found for ID {search_id}")
            break
        continue
    elif choice == 'd':
        os.system('cls')
        search_id = input("Please enter your ID number ----> ").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print(f"=========================\n\nRecord Found for ID {search_id}")
                # print the record for search id
                for i in student_record[search_id]:
                    print(f" --- {i}")
                print("=========================")

                student_record.pop(search_id)
                print("\nRecord Deleted")
            else:
                print(f"Sorry, no record found for ID {search_id}")
            break
        continue
    elif choice == 'e':
        print("---------------------------\n\nEdit/Modify Student's Record\n---------------------------")

        search_id = input("Please input your Id number ---> ").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print(f"\nRecord found for ID {search_id}")

                for i in student_record[search_id]:
                    print(f"--- {i}")
                print("---------------------------")

                id_no = input("Please enter your ID number ----> ")
                first_name = input("Please enter your first name ----> ")
                last_name = input("Please enter your last name ----> ")
                age = input("Please enter your age ----> ")
                section = input("Please enter your section ----> ")
                course = input("Please enter your course ----> ").upper()

                student_record[search_id][0] = first_name
                student_record[search_id][1] = last_name
                student_record[search_id][2] = age
                student_record[search_id][3] = course
                student_record[search_id][4] = section

                print("\nData updated Successfully")

            else:
                print("\nNo Record Found")
            break
        continue
    elif choice == 'f':
        os.system('cls')
        print("Export Student's Data")

        with open('students_records.json', 'w') as students_records:
            json.dump(student_record, students_records, indent = 4)

        print("\n\nData Exported to Json")

    elif choice == 'g':
        os.system('cls')

        print("Import Student's Data")
        with open('students_records.json', 'r') ac
            students_records:
            imported_records = json.load(students_records)

        print("\n\nData imported to json")

        continue
    elif choice == 'x':
        print("System Exit")
        break
    else:
        print("Invalid choice, re-enter your choice")
        continue