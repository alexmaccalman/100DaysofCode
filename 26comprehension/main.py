student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
   # print(value)
    pass



import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #print(row.student)
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

df = pd.read_csv("nato_phonetic_alphabet.csv")


#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}


# new_dict ={new_key:new_value for (key, value) in dict.items() if test}

phonetic_dic = {row.letter:row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter your name: ").upper()

# new_list = [new_item for item in list]
output = [phonetic_dic[letter] for letter in word]
print(output)
