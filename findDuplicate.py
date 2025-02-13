def remove_duplicates(input_list):
 
    seen = set()
    unique_list = []
    duplicates = []
    
    for item in input_list:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
        else:
            duplicates.append(item)
    
    return unique_list, duplicates


input_list = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7, 8, 6]
unique_list, duplicates = remove_duplicates(input_list)

print("Original List:", input_list)
print("List without duplicates:", unique_list)
print("Duplicates found:", duplicates)