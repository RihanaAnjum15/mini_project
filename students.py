#creating a dictionary variable
students = {} 

#creating a function to add a student 
def add_student(): 
    roll = input("Enter roll number: ") 
    name = input("Enter name: ") 
    marks = input("Enter marks: ") 
    students[roll] = {"name": name, "marks": marks} 
 
 # defining a function to view_students
def view_students(): 
    for roll, info in students.items(): 
        print(f"Roll: {roll}, Name: {info['name']}, Marks: 
{info['marks']}") 
     
 #creating a menu 
while True: 
    print("\n1. Add Student\n2. View Students\n3. Exit") 
    choice = input("Choose an option: ") 
     
    if choice == "1": 
        add_student() 
    elif choice == "2": 
        view_students() 
    elif choice == "3": 
        break 
    else: 
        print("Invalid choice")
