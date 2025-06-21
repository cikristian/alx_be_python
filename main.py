class person:
    def __init__(self, name, age,height=None, weight=None):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    def __BMI__(self):
        if self.height is not None and self.weight is not None:
            return self.weight / (self.height ** 2)
        else:
            return "Height and weight must be provided to calculate BMI."
    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, height={self.height}, weight={self.weight})"
    
    # Create an instance
# p1 = person("Alice", 30, height=1.7, weight=65)

# # Call methods and print output
# print(p1.greet())
# print(p1.__BMI__())
# print(p1) 

# 🟢 Collect user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters (e.g., 1.75): "))
weight = float(input("Enter your weight in kg (e.g., 70): "))

# 🟢 Create person instance
p2 = person(name, age, height, weight)

# 🟢 Show results
print(p2.greet())
print(f"Your BMI is: {p2.__BMI__():.2f}")
print(p2)
print(f"Your name is {p2.name}, your age is {p2.age}, your height is {p2.height} meters, and your weight is {p2.weight} kg and you BMI is {p2.__BMI__():.2f}.")