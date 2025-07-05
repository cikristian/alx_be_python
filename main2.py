class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person object created: {self.name}, {self.age} years old.")

    def __del__(self):
        print(f"Goodbye from {self.name}! The Person object is being deleted.")

# Example usage:
p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

print(f"{p1.name} is {p1.age} years old.")
print(f"{p2.name} is {p2.age} years old.")

# Delete an object explicitly (optional, normally handled by garbage collector)
del p1

# p2 will be deleted automatically at end of program
