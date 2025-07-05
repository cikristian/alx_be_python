class info:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

name1 = input("Enter your name: ")
age1 = int(input("Enter your age: "))
# Create an instance of the info class 
person_info = info(name1, age1)
# Display the information  
person_info.display()
# Create another instance with different data  
print(f"My name is {person_info.name} and I am {person_info.age} years old. I am a software engineer.")