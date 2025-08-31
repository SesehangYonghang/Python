#Greeting Card Function
name = input("Enter your name: ")
age = input("Enter your age: ")
def make_card(name, age, message = "Have a good day."):
    card = f"Hello {name}, ({age} years old!)\n{message}"
    return card

print(make_card(name,age))

