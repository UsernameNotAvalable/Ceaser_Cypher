import string

def Finished():
    task_done = input ("When you are finished reading, please press enter to end program.")
    

# def remove_spaces(text):
#     return text.replace(" ", "")


# def convert_to_uppercase(text):
#     return text.upper()


def conversionCeaser(text):
    words = ' '
    text = text.upper().replace(",","X")
    for each in text:
        if each  not in string.ascii_uppercase:
            continue
        else:
            words += each
    return words

def encrypt(text, shift):
    encrypted = ""
    for c in text:
        if c == '.':
            encrypted += 'X'
        elif c in string.ascii_uppercase:
            index = (string.ascii_uppercase.index(c) + shift) % 26
            encrypted += string.ascii_uppercase[index]
        else:
            encrypted += c
    return encrypted

# usage
print("Welcome to the ceaser cypher!")
plaintext = input("Enter your sentence you want to be encrypted (Alphabetical inputs only): ")
shift = int(input("Enter the cypher key (Numerical): "))


# # Encryption
# plaintext = remove_spaces(plaintext)
plaintext = conversionCeaser
encrypted = encrypt(plaintext, shift)
print("Ciphertext:", encrypted)
print("Thank you for using the cypher, please use the program again when needed!")
#Finished()

