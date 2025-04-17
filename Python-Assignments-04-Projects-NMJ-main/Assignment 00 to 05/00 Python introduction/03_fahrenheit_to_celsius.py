# Ask the user for the temperature in Fahrenheit and convert it into Celsius
def main():
    print("Convert temperature from fahrenheit to celsius")
    try:
        fahrenheit = float(input("Enter temperature in fahrenheit"))
        convert_in_celcius = (fahrenheit - 32) * 5.0/9/0
        print(f"Temperature : {fahrenheit}F = {convert_in_celcius}C")
    except ValueError:
        print("Please Enter a valid temperature value")    
    
if __name__ == "__main__":
    main()    