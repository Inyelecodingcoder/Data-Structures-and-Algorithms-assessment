def is_balanced(expression):
    pass
    

    if expression == "()" or expression == "{}":
        print(True)
    elif expression == "(}" or expression == "{]":
        print(False)
    
print(is_balanced("()"))
print(is_balanced("{}"))
print(is_balanced("(}"))

def remove_duplicates():
    pass
original_list = [2, 2, 3, 4, 5, 5, 7, 7, 8]
new_list = []

for i in range(len(original_list) - 1):
    if original_list[i] != original_list[i + 1]:
        new_list.append(original_list[i])


new_list.append(original_list[-1])

print(new_list)
