# Temperature conversion program

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Main program loop
while True:
    # Display menu
    print("Select temperature conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    # Take input from the user
    choice = input("Enter choice (1/2): ")

    # Check if choice is one of the two options
    if choice in ('1', '2'):
        # Take input from the user for the temperature to convert
        temp = float(input("Enter temperature: "))

        # Perform the selected conversion
        if choice == '1':
            converted_temp = celsius_to_fahrenheit(temp)
            print(temp, "Celsius =", converted_temp, "Fahrenheit")

        elif choice == '2':
            converted_temp = fahrenheit_to_celsius(temp)
            print(temp, "Fahrenheit =", converted_temp, "Celsius")
        break
    else:
        print("Invalid Input")
