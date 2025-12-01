def celsius_to_fahrenheit(celsius):

    return (celsius * 1.8) + 32

def fahrenheit_to_celsius(fahrenheit):

    return (fahrenheit -32) / 1.8

def get_valid_number(prompt):

    while True:
        try:
            user_input = input(prompt)
            value = float(user_input)

            return value
        except ValueError:

            print("Error: Please enter a valid number!")

def main():
    
    print("--- Temperature Converter Project ---")
    print("1. Celsius -> Fahrenheit")
    print("2. Fahrenheit -> Celsius")
    print("3.Exit")

    while True:
        choice = input("\nYour Choice (1/2/3):")

        if choice == "1":

            c = get_valid_number("Enter degrees Celsius: ")
            f = celsius_to_fahrenheit(c)

            print(f"Result: {c}°C = {f:.2f}°F")

        elif choice == "2":

            f = get_valid_number("Enter degrees Fahrenheit: ")
            c = fahrenheit_to_celsius(f)

            print(f"Result: {c}°C = {f:.2f}°C")

        elif choice == "3":
            print("Exiting the program...")
            break
        
        else:
            print("Invalid selection, please select 1, 2 or 3.")

if __name__ == "__main__":
    main()