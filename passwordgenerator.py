import random

print("Welcome To Your Password Generator")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*(),.:0123456789"

number = input("Amount of Passwords to generate: ")
number = int(number)

length = input("Input Your Passwords Length: ")
length = int(length)

print("here are your passwords: ")

for passwords in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
        print(passwords)
