class Dog:
    def __init__(self, name):
        self.name = name  # self.name belongs to this specific dog

# Using positional argument
dog1 = Dog("Buddy")

# Using named argument (same result)
dog2 = Dog(name="Max")

# Each dog has its own name
print(dog1.name)  # Buddy
print(dog2.name)  # Max