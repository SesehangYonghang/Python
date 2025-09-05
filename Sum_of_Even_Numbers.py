# Sum of even numbers using loops
n = int(input("Enter a positive integer: "))
def main():
    Sum_of_even_numbers()
def Sum_of_even_numbers():
    total = 0
    for i in range(1,n + 1):
        if i % 2 == 0:
            total += i
            print("Sum of even numbers upto ", n, "is", total)
 
main()         
