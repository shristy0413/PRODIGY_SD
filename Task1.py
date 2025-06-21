unit = input("Is this temperature in Celsius, Fahrenheit, or Kelvin (C/F/K): ").upper()
temp = float(input("Enter the temperature: "))

if unit == "C":
    f = round((9 * temp) / 5 + 32, 1)
    k = round(temp + 273.15, 1)
    print(f"The temperature in Fahrenheit is: {f}°F")
    print(f"The temperature in Kelvin is: {k}K")

elif unit == "F":
    c = round((temp - 32) * 5 / 9, 1)
    k = round((temp - 32) * 5 / 9 + 273.15, 1)
    print(f"The temperature in Celsius is: {c}°C")
    print(f"The temperature in Kelvin is: {k}K")

elif unit == "K":
    c = round(temp - 273.15, 1)
    f = round((temp - 273.15) * 9 / 5 + 32, 1)
    print(f"The temperature in Celsius is: {c}°C")
    print(f"The temperature in Fahrenheit is: {f}°F")

else:
    print(f"{unit} is an invalid unit of measurement.")