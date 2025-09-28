import os

print("Hello from Docker!")


DEFAULT_STUDENT_NAME = "Alice Wonderland"

student_name = os.getenv('STUDENT_NAME', DEFAULT_STUDENT_NAME)


if os.getenv('STUDENT_NAME'):
    
    print(f"Student Name (STUDENT_NAME) [Set via Environment]: {student_name}")
else:
    
    print(f"No student name provided (STUDENT_NAME is not set). Displaying default: {student_name}")
