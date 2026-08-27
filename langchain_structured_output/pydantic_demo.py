from pydantic import BaseModel, Field  ,EmailStr
from typing import Optional


class Student(BaseModel):  
    name: str = Field(..., title="Student Name", description="The full name of the student")  
    age: Optional[int] = None 
    email: EmailStr
    gpa: float = Field(ge=0.0, le=4.0,default = 4.0, title="Student GPA", description="The GPA of the student, must be between 0.0 and 4.0")

new_student = {'name': 'John Doe','age':'32', 'email': 'john.doe@xample.com'}

student = Student(**new_student)  # This will create a Student instance and print it
student_dict =(dict(student))

print(student_dict['age'])  # Output: 32

student_json = student.model_dump_json()  # This will create a JSON representation of the Student instance
print(student_json)