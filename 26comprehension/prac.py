with open("file1.txt") as file1:
    list1 = file1.readlines()

with open("file2.txt") as file2:
    list2 = file2.readlines()

# in list can be any iterable
# new_list = [new_item for item in list]

new_list = [int(num) for num in list1 if num in list2]

print(new_list)