def celsius_to_kelvin(celsius: float) -> float:
    return celsius + 273.15

def kelvin_to_celsius(kelvin: float) -> float:
    return kelvin - 273.15

def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5/9

def kelvin_to_fahrenheit(kelvin: float) -> float:
    return (kelvin - 273.15) * 9/5 + 32

def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5/9 + 273.15


celsius_temp = float(input("Enter temperature in Celsius: "))
kelvin_temp = celsius_to_kelvin(celsius_temp)
print(f"{celsius_temp} Celsius is equal to {kelvin_temp} Kelvin.")

kelvin_temp = float(input("Enter temperature in Kelvin: "))
celsius_temp = kelvin_to_celsius(kelvin_temp)
print(f"{kelvin_temp} Kelvin is equal to {celsius_temp} Celsius.")

fahrenheit_temp = float(input("Enter temperature in Fahrenheit: "))
celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp} Fahrenheit is equal to {celsius_temp} Celsius.")

celsius_temp = float(input("Enter temperature in Celsius: "))
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp} Celsius is equal to {fahrenheit_temp} Fahrenheit.")

kelvin_temp = float(input("Enter temperature in Kelvin: "))
fahrenheit_temp = kelvin_to_fahrenheit(kelvin_temp)
print(f"{kelvin_temp} Kelvin is equal to {fahrenheit_temp} Fahrenheit.")

fahrenheit_temp = float(input("Enter temperature in Fahrenheit: "))
kelvin_temp = fahrenheit_to_kelvin(fahrenheit_temp)
print(f"{fahrenheit_temp} Fahrenheit is equal to {kelvin_temp} Kelvin.")
