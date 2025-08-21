#Global Variable
num_1 = 5
def displaynum():
    global num_1
    num_1 = 6
    num_2 = 7 #Local Variable
    return num_1, num_2
print(num_1)
print(displaynum())
