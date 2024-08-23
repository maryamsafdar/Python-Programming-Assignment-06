def manage_student_database():
    students = []
    student_id = 1
    
    while True:
        name = input("Please enter the student's name (or type 'stop' to finish): ")
        
        if name.lower() == 'stop':
            break
        
        # Check for duplicate names
        if any(student[1] == name for student in students):
            print("This name is already in the list.")
            continue
        
        # Add new student to the list
        students.append((student_id, name))
        student_id += 1
    
    # Display complete list of students
    print("\nComplete List of Students (Tuples):")
    print(students)
    
    # Display each student with ID and name
    print("\nList of Students with IDs:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}")
    
    # Calculate total number of students
    total_students = len(students)
    print(f"\nTotal number of students: {total_students}")
    
    # Calculate total length of all student names combined
    total_name_length = sum(len(student[1]) for student in students)
    print(f"Total length of all student names combined: {total_name_length}")
    
    # Identify the student with the longest and shortest name
    if students:
        longest_name_student = max(students, key=lambda student: len(student[1]))[1]
        shortest_name_student = min(students, key=lambda student: len(student[1]))[1]
        print(f"The student with the longest name is: {longest_name_student}")
        print(f"The student with the shortest name is: {shortest_name_student}")

# Call the function to run the program
manage_student_database()
