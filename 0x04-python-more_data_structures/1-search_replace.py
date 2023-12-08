#!/usr/bin/python3
# Write a function that replaces all occurrences of an element by another in a new list.


# Prototype: def search_replace(my_list, search, replace):
# my_list is the initial list
# search is the element to replace in the list
# replace is the new element
# You are not allowed to import any module
def search_replace(my_list, search, replace):
    new_list = []
    for item in my_list:
        if search == item:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list


my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)

# if __name__ == "__main__":
#     search_replace()
