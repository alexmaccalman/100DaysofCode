#TODO: Create a letter using starting_letter.txt 
with open("./Input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()
 #for each name in invited_names.txt

with open("./Input/Letters/starting_letter.txt", mode="r") as file:
    starting_letter = file.read()

for name in names:
    name = name.strip()
    #Save the letters in the folder "ReadyToSend".
    with open(f"./Output/ReadyToSend/{name}_letter.txt", mode="w") as file:
        #Replace the [name] placeholder with the actual name.
        new_letter = starting_letter.replace("[name],", f"{name},")
        file.write(new_letter)










    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp