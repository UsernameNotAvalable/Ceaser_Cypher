import string


# Double click option of running program - allows users to read the terminals and proceed when ready.
def Finished():
    task_done = input("When you are finished reading, please press enter to end program.")


# Strips everything that is not an ascii uppercase (symbols and spaces) and adds into the output.
def conversionCeaser(text):
    words = " "
    text = text.upper()
    for each in text:
        if each == ".":
            each = "X"
        if each not in string.ascii_uppercase:
            continue
        else:
            words += each
    return words


# maps text input and replaces all "." with X as required - gets all ascii uppercases and shifts thier indexed letter (encrypts)
def encrypt(text, shift):
    encrypted = ""
    for c in text:
        if c in string.ascii_uppercase:
            index = (string.ascii_uppercase.index(c) + shift) % 26
            encrypted += string.ascii_uppercase[index]
        else:
            encrypted += c
    return encrypted


# usage
print("Welcome to the ceaser cypher!")
plaintext = input("Enter your sentence you want to be encrypted (Alphabetical inputs only): ")
shift = int(input("Enter the cypher key (Numerical): "))

# Encryption, places the inputs from user into the encryption function
#plaintext = conversionCeaser(plaintext)
print(conversionCeaser(plaintext))
stripped = conversionCeaser(plaintext)
# strips all inputs that are unwanted (symbols etc)
encryptedText = encrypt(stripped, shift)
print("Ciphertext:", encryptedText)
print("Thank you for using the cypher, please use the program again when needed!")
Finished()
