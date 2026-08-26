class Students :
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

students = Students("Alice", 20, "A")
students.say_hello()  # 输出: Hello, my name is Alice and I am 20 years old.
