# Initialize a variable 'clothes' with the value 'Dirty Clothes'
clothes = 'Dirty Clothes'

# Define a function named 'washingmachine'
def washingmachine():
    # Use the global keyword to access and modify the global variable 'clothes'
    global clothes
    # Set the variable 'clothes' to 'Clean Clothes'
    clothes = 'Clean Clothes'
    # Return the updated value of 'clothes'
    return clothes

# Print the current value of 'clothes'
print(clothes)

# Call the 'washingmachine' function, which updates 'clothes' and returns the new value
print(washingmachine())
