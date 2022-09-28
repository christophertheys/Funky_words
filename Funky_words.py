# Compulsory Task 1
# The program will capitalise each alternative letter

word = input("Enter a sentence : ")

adjusted_word = word[::2].upper()
adjusted2_word = word[1::2].lower()
print(''.join(x + y for x, y in zip(adjusted_word, adjusted2_word)))

# Did some research on how to capitalise alternating letters using the 'zip' function. This will combine the declared
# x variable assigned 'adjusted_word' and y variable assigned 'adjusted2_word'
