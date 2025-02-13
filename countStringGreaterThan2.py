def count_strings(strings_list):
    
    count = 0
    for string in strings_list:
        if len(string) > 2:
            count += 1
            print(string)
   
    return count

# Example usage
strings_list = ["a", "abc", "de", "", "xyz", "1234", "hi"]
result = count_strings(strings_list)

print("Number of strings with length 2 or more:", result)


#first & last char is same

def count_special_strings(strings_list):
    count = 0
    for string in strings_list:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

# Example usage
strings_list = ["abc", "aba", "xyz", "adr", "121", "b"]
result = count_special_strings(strings_list)

print("Number of special strings:", result)