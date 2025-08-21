#Greeting Card Function
def make_card(name = None, age = None, message = "Have a good day."):
    if name is None:
        name = input("Enter your Name: ")
    
    if age is None:
        age = input("Enter your age: ")
    
    card = f"Hello {name}({age} years old)!\n{message}"
    return card

print(make_card())
