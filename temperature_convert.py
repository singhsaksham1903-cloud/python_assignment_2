def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

n = float(input("enter the temperature in celsius: "))
print("the temperature in fahrenheit is: ", celsius_to_fahrenheit(n))