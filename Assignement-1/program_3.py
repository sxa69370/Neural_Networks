# Question: Write a program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’. 
# • Sample input: I love playing with python 
# • Sample output: I love playing with pythons 

# input sentence from the user
sentence = input("Enter a sentence: ")

# Splitting the sentence into a list of words
sentence = sentence.split()

# Replacing the string 'python' occurences with 'pythons' string in a sentence. But not any already existing 'pythons' string a sentence
# Joining the list into a sentence with a space inbeteween the words.

modified_sentence = ' '.join('pythons' if word.lower() == 'python' else word for word in sentence)

# Print the modified sentence
print("Modified sentence: ",  modified_sentence)