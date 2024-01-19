# Write a python program to find the wordcount in a file (input.txt) for each line and then print the output. Finally store the output in output.txt file. 

def wordcount():
    output = dict()
    words = []
    count = 0
    # Opened the input.txt file in read mode
    with open("input.txt","r") as input_file:

        # fetching each line from input.txt file using for loop and separating the words using split function
        for i in input_file.readlines():
            words = words + [i for i in i.split()]

        # Storing the occurences of a word using dictionary
        for word in words:
            output[word] = output.get(word,0) + 1

    # Opening the output.txt file with below command, if it doesn't exist it creates
    with open("output.txt","w") as output_file:
        
        # fetching the key, value pair from dictionary using for loop
        for key in output:
            # Writing the key, value onto the output.txt file
            output_file.write("{}: {}\n".format(key,output[key]))
            
if __name__ == '__main__':
    wordcount()
