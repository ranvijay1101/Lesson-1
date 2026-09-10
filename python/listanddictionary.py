classmates = ["Aarav", "Samar", "Mudit", "Tweesha", "Reyansh"]
print("Class list:", classmates)
print("Total students:", len(classmates))
print("First student:", classmates[0])
print("Last student:", classmates[-1])
print("First three students:", classmates[:3])
classmates.append("Bob")
print("\nUpdated class list:", classmates)
classmates.remove("Aarav")  
print("Updated class list after removing Aarav:", classmates)
classmates.sort()
print("Sorted alphabetically:", classmates)
classmates.reverse()
print("Reversed:", classmates)
teacher = {"name": "Mr. Smith", "subject": "Math", "age": 40}
print("\nTeacher profile:", teacher)
print("Subject:", teacher["subject"])
print("Experience:", teacher.get("experience", "Not found"))
teacher["experience"] = 6
teacher["email"] = "idk@gmail.com"
print("Updated teacher profile:", teacher)
roll_numbers = [1, 2, 3, 4, 5]
names = ["Aarav", "Samar", "Mudit", "Tweesha", "Reyansh"]
student_directory = dict(zip(roll_numbers, names))
print("\nStudent Directory:", student_directory)
print("Student with roll number 3:", student_directory[3])