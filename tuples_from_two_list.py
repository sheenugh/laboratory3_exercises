list1 = [1,2,3]
list2 = ["mark","alice","john"]

tuples_from_two_lists = [(n,m) for n, m in zip(list1, list2)]
print(f"result: listOfTuple{tuples_from_two_lists}") # - Relied on the camel case from the instruction for the output