def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

print("Unit Converter Options:")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
print("3. Kilograms to Pounds")
print("4. Pounds to Kilograms")
print("5. Celsius to Fahrenheit")
print("6. Fahrenheit to Celsius")

choice = input("Enter the number of the conversion you want: ")

try:
    if choice == '1':
        km = float(input("Enter distance in kilometers: "))
        print(f"{km} km = {km_to_miles(km)} miles")
    elif choice == '2':
        miles = float(input("Enter distance in miles: "))
        print(f"{miles} miles = {miles_to_km(miles)} km")
    elif choice == '3':
        kg = float(input("Enter weight in kilograms: "))
        print(f"{kg} kg = {kg_to_pounds(kg)} pounds")
    elif choice == '4':
        pounds = float(input("Enter weight in pounds: "))
        print(f"{pounds} pounds = {pounds_to_kg(pounds)} kg")
    elif choice == '5':
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C = {celsius_to_fahrenheit(c)}°F")
    elif choice == '6':
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f}°F = {fahrenheit_to_celsius(f)}°C")
    else:
        print("Invalid choice.")
except ValueError:
    print("Please enter a valid number.")
