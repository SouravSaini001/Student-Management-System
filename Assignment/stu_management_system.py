student = {
    "Sourav": 99,
    "Aman": 88,
    "Rahul": 92,
    "Priya": 95,
    "Neha": 87,
    "Rohit": 91,
    "Anjali": 94,
    "Vikas": 78,
}

while True:

    print("\n========== Student Management System ==========")
    print("A. Add Student")
    print("B. Update Marks")
    print("C. Search Student")
    print("D. Display All Students")
    print("E. Delete Student")
    print("F. Show Topper")
    print("G. Show Lowest Marks")
    print("H. Average Marks")
    print("I. Students Above Given Marks")
    print("J. Sort by Marks")
    print("K. Total Students")
    print("L. Exit")

    op = input("\nEnter Operation: ").upper()

    if op == "A":
        name = input("Enter Name: ")

        if name in student:
            print("Student already exists!")
        else:
            marks = int(input("Enter Marks: "))
            student[name] = marks
            print("Student Added Successfully!")

    elif op == "B":
        name = input("Enter Name: ")

        if name in student:
            marks = int(input("Enter New Marks: "))
            student[name] = marks
            print("Marks Updated Successfully!")
        else:
            print("Student Not Found!")

    elif op == "C":
        name = input("Enter Name: ")

        if name in student:
            print(f"{name} scored {student[name]} marks.")
        else:
            print("Student Not Found!")

    elif op == "D":
        print("\nStudent List")
        for name, marks in student.items():
            print(f"{name:10} : {marks}")

    elif op == "E":
        name = input("Enter Name to Delete: ")

        if name in student:
            del student[name]
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found!")

    elif op == "F":
        topper = max(student, key=student.get)
        print(f"Topper: {topper} ({student[topper]} marks)")

    elif op == "G":
        lowest = min(student, key=student.get)
        print(f"Lowest: {lowest} ({student[lowest]} marks)")

    elif op == "H":
        avg = sum(student.values()) / len(student)
        print(f"Average Marks: {avg:.2f}")

    elif op == "I":
        limit = int(input("Enter Minimum Marks: "))

        print("\nStudents Scoring Above", limit)

        found = False
        for name, marks in student.items():
            if marks > limit:
                print(name, "-", marks)
                found = True

        if not found:
            print("No Student Found.")

    elif op == "J":
        sorted_students = sorted(student.items(), key=lambda x: x[1], reverse=True)

        print("\nStudents Sorted by Marks")
        for name, marks in sorted_students:
            print(name, "-", marks)

    elif op == "K":
        print("Total Students:", len(student))

    elif op == "L":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")