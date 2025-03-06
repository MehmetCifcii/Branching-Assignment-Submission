def package_express():
    print("Welcome to Package Express. Please follow the instructions below.")
    
    # Prompt user for package weight
    weight = float(input("Please enter the package weight: "))
    
    # Weight check
    if weight > 50:
        print("Package too heavy to be shipped via Package Express. Have a good day.")
        return
    
    # Prompt user for package width
    width = float(input("Please enter the package width: "))
    
    # Prompt user for package height
    height = float(input("Please enter the package height: "))
    
    # Prompt user for package length
    length = float(input("Please enter the package length: "))
    
    # Total dimension check
    if (width + height + length) > 50:
        print("Package too big to be shipped via Package Express.")
        return
    
    # Price calculation
    quote = (width * height * length * weight) / 100
    
    # Display result
    print(f"Your estimated total for shipping this package is: ${quote:.2f}")
    print("Thank you!")

# Run the program
package_express()
