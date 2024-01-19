# Question: Input the string “Python” as a list of characters from console, 
# delete at least 2 characters,reverse the resultant string and print it. 
# Sample input: python 
# Sample output: ntyp 

# Enter the string
string = input("Enter a string: ")

# Delete at least 2 characters
if len(string) > 2:
    modified_string = string[:-3] + string[-1:]

    # Reverse the modified string
    reversed_string = modified_string[::-1]
    print("Reversed string: ",reversed_string)
else:
    print("Enter a string with at least 2 characters.")
