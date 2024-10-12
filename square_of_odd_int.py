list1 = [2, 4, 3]
list2 = [0, 0, 1, 1]
square_of_odd_integer_element_for_list1= [num**2 for num in list1 if num %2 ==1]
square_of_odd_integer_element_for_list2= [num**2 for num in list2 if num %2 ==1]
print(f"{list1} == {square_of_odd_integer_element_for_list1}")
print(f"{list2} == {square_of_odd_integer_element_for_list2}")

# - I copied the format of the output written on the instruction.