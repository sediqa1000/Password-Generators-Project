import random
letters =list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers =list( "0123456789")
symbols =list("!@#$%^&*()-+=><:;/~")

print("welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n "))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
password_list = []
for _ in range (nr_letters):
    password_list.append(random.choice(letters))
for _ in range (nr_numbers):
    password_list.append(random.choice(numbers))
for _ in range (nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password = "".join(password_list)
print(password)

