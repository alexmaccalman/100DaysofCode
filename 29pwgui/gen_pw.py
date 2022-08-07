from random import choice, randint, random, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# new_list = [new_item for item in list]

pw_letters = [choice(letters) for _ in range(randint(8,10))]

pw_numbers = [choice(numbers) for _ in range(randint(2, 4))]
pw_symbols = [choice(symbols) for _ in range(randint(2, 4))]

pw_list = pw_letters + pw_numbers + pw_symbols


shuffle(pw_list)

pw = "".join(pw_list)
print(pw)