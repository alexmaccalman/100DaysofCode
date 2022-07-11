try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["not_a_key"])
except FileNotFoundError:
    open("a_file.txt", mode="w")
    file.write("Something")
except KeyError as error_message: #this wll show the error message
    print(f"The key {error_message} does not exist")
else: # when the thing we are trying does succeed
    content = file.read()
    print(content)
finally: # runs no matter what happens
    file.close()
    print("File was closed")


