FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    temp = float(input("Enter the temperature value: "))
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")

unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == "C":
    converted = convert_to_fahrenheit(temp)
    print(f"{temp}°C is {converted:.2f}°F")
elif unit == "F":
    converted = convert_to_celsius(temp)
    print(f"{temp}°F is {converted:.2f}°C")
else:
    print("Invalid unit entered. Please enter 'C' for Celsius or 'F' for Fahrenheit.")