from temperature.celsius_to_farenheit import celsius_to_fahrenheit
from temperature.farenheit_to_celsius import fahrenheit_to_celsius
from temperature.celsius_to_kelvin import celsius_to_kelvin

def main():
    while True:
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Quit")
        
        choice = input("Select option (1-4): ").strip()
        
        if choice == '4':
            print("Goodbye!")
            break
        
        try:
            temp = float(input("Enter temperature value: "))
            
            if choice == '1':
                result = celsius_to_fahrenheit(temp)
                print(f"{temp}°C = {result:.2f}°F")
            elif choice == '2':
                result = fahrenheit_to_celsius(temp)
                print(f"{temp}°F = {result:.2f}°C")
            elif choice == '3':
                result = celsius_to_kelvin(temp)
                print(f"{temp}°C = {result:.2f}K")
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
 main()
