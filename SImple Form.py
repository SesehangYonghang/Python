def getNickname(name: str) -> str:
    parts = name.split()
    if len(parts) == 1:
        return parts[0]
    else:
        return parts[0][:2] + parts[-1][-2:]


name = input("Please Enter your Full name:\t").strip()
age = input("Enter your age:\t").strip()
height_input = input("Enter your height in feet:\t").strip()
country = input("Enter your country name:\t").strip()

if not name or not age or not height_input or not country:
    print("\nPlease enter all required data!")
else:
    try:
        height = float(height_input) 
        print(f"\nHello {name.upper()}")
        print(f"You are {age} years old.")
        print(f"Your height is {round(height, 2)} feet.")
        print(f"You are from {country.capitalize()}.")
        print(f"Your Nickname is {getNickname(name).upper()}")
    except ValueError:
        print("\nHeight must be a valid number!")
