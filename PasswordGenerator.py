import random
import math

def letter():
    return random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[]^_`{|}~") + random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[]^_`{|}~") + random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[]^_`{|}~")

def meow():
    randbits = random.getrandbits(random.randint(0, 400))
    rundum = random.randint(1, 30)
    number = rundum + randbits
    how_much = input("How many lines of passwords do you want?""\n")
    max_num = int(input("How many characters do you want?""\n"))

    for i in range(int(how_much)):
        password1 = str(random.randint(int(rundum), int(math.pow(randbits, 2)) - 1)) + random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[]^_`{|}~")
        password2 = str(random.randint(randbits - number, randbits - 1)) + random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[]^_`{|}~")
        password3 = str(abs(random.randint(rundum, int(math.pow(randbits, 2) - 1) - random.randint(randbits - number, randbits)))) + random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[]^_`{|}~")
        password4 = str(int(random.randint(randbits, number - 1))) + random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[]^_`{|}~")
        password5 = str(password1 + password2) + letter()
        password6 = str(password3 + password4) + letter()

        kitty = letter() + letter() + password5 + letter() + letter() + password6 + letter() + letter()
        cat = kitty[:max_num]
        cat = cat
        print(cat)

print("______                                   _                                   _")
print("| ___ \\                                 | |                                 | |")
print("| |_/ /_ _ ___ _____      _____  _ __ __| |   __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __")
print("|  __/ _` / __/ __\\ \\ /\\ / / _ \\| '__/ _` |  / _` |/ _ \\ '_ \\ / _ \\ '__/ _` | __/ _ \\| '__|")
print("| | | (_| \\__ \\__ \\\\ V  V / (_) | | | (_| | | (_| |  __/ | | |  __/ | | (_| | || (_) | |")
print(r"\_|  \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|")
print("                                              __/ |")
print("                                             |___/")

meow()
