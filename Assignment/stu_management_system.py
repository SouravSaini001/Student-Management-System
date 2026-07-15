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

op = input("What operation to Perform : ")
if(op == "A"):
    name = input("Enter your name here : ")
    marks = input("Enter your marks here : ")
    student.update({name : marks})
    print("Added Successfully")
    print(student)
elif(op == "B"):
    name = input("Enter your name : ")
    if student.get(name) != None:
        marks = input("Enter your marks here : ")
        student[name] = marks
        print("Marks updated Successfully!")
        print(student)
elif(op == "C"):
    name = input("Enter your name here : ")
    if student.get(name) != None:
        print(f"Congrulations the user found with this name : ")
    else:
        print("Sorry the user not found!")
elif(op == "D"):
    print(student)
else:
    print("Invalid Operation!")

    
