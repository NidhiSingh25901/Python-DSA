list1 = [12, "Hello", 3.45, None, True, [1,2,3], (4,5,6),[2,3,45,5,5], {'a':1, 'b':2}] 

for i in range(len(list1)): 
    print(f"Element at index {i} is {list1[i]} and its data type is {type(list1[i])}")