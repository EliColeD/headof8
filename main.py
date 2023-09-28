def convert(gallons):
    try:  # Try block
        if gallons < 0:
            raise ValueError
        liters = gallons * 3.785  # gallons conversion to liters
        return liters

    except ValueError:  # exception block
        print("The entered value is negative !!!")


# driver code
x = float(input("Enter the number of gallons : "))
print(x, "gallons = ", convert(x), " liters")
