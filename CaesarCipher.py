#Caesar Cipher
# Write a Python program that encrypts text given by the user. 
# The program should ask the user for a plain text sentence and print the encrypted text. 
# The text should be encrypted using a caesar cipher with a right shift of 5.

abc = "abcdefghijklmnopqrstuvwxyz"
plain_text = input("Please enter a plain text sentence: ")
plain_text = plain_text.lower()
shift = 5

encrypted_text = " "

for char in plain_text:
    if char in abc:
        position = abc.find(char)
        position = (position + shift) % 26
        char = abc[position]
    encrypted_text += char
print(encrypted_text)
  

