def alternate_even_odd(input_list):
    
    even_list = [num for num in input_list if num % 2 == 0]
    odd_list = [num for num in input_list if num % 2 != 0]

   
    result = []
    i = 0
    while i < len(even_list) and i < len(odd_list):
        result.append(even_list[i])
        result.append(odd_list[i])
        i += 1

   
    result.extend(even_list[i:]) #slicing of array [start:end:step]
    result.extend(odd_list[i:])

    return result

# Example usage
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = alternate_even_odd(input_list)

print("Original List:", input_list)
print("List with alternate even and odd numbers:", result)