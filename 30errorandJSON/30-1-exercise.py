fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
        
    except IndexError: # if there is a Index error then print this
        print("Fruit pie")
    else:
        print(fruit + " pie") # run this when there is no error


make_pie(2)
