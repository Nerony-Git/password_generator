import string
import random


def pass_gen():
    #Generate all uppercase letters
    str1 = string.ascii_uppercase

    #Generate all lowercase letters
    str2 = string.ascii_lowercase

    #Generate all numbers
    str3 = string.digits

    #Generate special characters
    str4 = string.punctuation

    #Receive input of length of password from user
    length_password = int(input("Enter your preferred password length :\n"))

    #Creating an array to store all letters, numbers and special characters.
    password = []
    password.extend(list(str1))
    password.extend(list(str2))
    password.extend(list(str3))
    password.extend(list(str4))

    #Select from array randomly and shuffle.
    random.shuffle(password)

    #generate password according to the length of characters the user input
    generated_password = "Generated Password : " + ("".join(password[0 : length_password]))

    print(generated_password)


pass_gen()