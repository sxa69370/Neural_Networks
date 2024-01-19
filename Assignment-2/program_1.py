#Question: Write a program that takes two strings from the user: first_name, last_name. Pass these variables to fullname function that should return the (full name). 
# o For example: ▪ First_name = “your first name”, last_name = “your last name”
# ▪ Full_name = “your full name” 
# o Write function named “string_alternative” that returns every other char in the full_name string. 
# Str = “Good evening” 
# Output: Go vnn 

firstname = input("Enter First Name: ")
lastname = input("Enter Last Name: ")

# concatinating the strings with '+' symbol
def fullname(firstname,lastname):
    return lastname +" "+ firstname

def string_alternative(s):
    output = ""
    # iterating each character of string
    for i in s:
        # If the character is  not present in output, then adds to it, if not skips the character. So only unique characters stored in output
        if i not in output:
            output = output + i
    return output  

if __name__ == '__main__':
    full_name = fullname(firstname,lastname)
    unique_characters = string_alternative(full_name)
    print("fullname : {}, Output from string alternative function: {}".format(full_name,unique_characters))
