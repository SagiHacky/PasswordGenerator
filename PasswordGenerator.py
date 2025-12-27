import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!#$%&()*+,-./:;<=>?@[]^_`{|}~"
all_chars = letters + numbers + symbols

def make_password(length):
    password = [
        random.choice(letters),
        random.choice(numbers),
        random.choice(symbols)
    ]
    for _ in range(length - 3):
        password.append(random.choice(all_chars))
    random.shuffle(password)
    return "".join(password)

def meow():
    lines = int(input("How many lines of passwords do you want?\n"))
    length = int(input("How many characters do you want?\n"))
    if length < 3:
        print("Password length must be at least 3")
        return
    for _ in range(lines):
        print(make_password(length))

print("______                                   _                                   _")
print("| ___ \\                                 | |                                 | |")
print("| |_/ /_ _ ___ _____      _____  _ __ __| |   __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __")
print("|  __/ _` / __/ __\\ \\ /\\ / / _ \\| '__/ _` |  / _` |/ _ \\ '_ \\ / _ \\ '__/ _` | __/ _ \\| '__|")
print("| | | (_| \\__ \\__ \\\\ V  V / (_) | | | (_| | | (_| |  __/ | | |  __/ | | (_| | || (_) | |")
print(r"\_|  \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|")
print("                                              __/ |")
print("                                             |___/")

meow()
