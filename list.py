my_list = [1, 2, 3, 4, 5]
print("\nList :")
print("\t", my_list)

print("\nSlicing:")
print("\t", my_list[1:3])

my_list.append(6)
print("\nAppending elements:")
print("\t", my_list)

my_list.insert(2, 10)
print("\nInserting elements at a specific index:")
print("\t", my_list)

my_list.remove(3)
print("\nRemoving elements:")
print("\t", my_list)

popped_element = my_list.pop(2)
print("\nPopped element:")
print("\t", popped_element)
print("List after popping:")
print("\t", my_list)

index = my_list.index(4)
print("\nIndex of element 4:")
print("\t", index)

is_present = 5 in my_list
print("\nIs 5 present in the list?")
print("\t", is_present)

length = len(my_list)
print("\nLength of the list:")
print("\t", length)

my_list.sort()
print("\nSorted list:")
print("\t", my_list)

my_list.reverse()
print("\nReversed list:")
print("\t", my_list)

new_list = my_list.copy()
print("\nCopied list:")
print("\t", new_list)

my_list.clear()
print("\nList after clearing:")
print("\t", my_list)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nNested List:")
print("\t", nested_list)

squares = [x**2 for x in range(5)]
print("\nList comprehensions:")
print("\t", squares)

print("\nIterating over the copied list:")
for item in new_list:
    print("\t", item)
