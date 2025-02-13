dict1 = {
    101: {"Apple": 10, "Mango": 5},
    102: {"Apple": 15, "Mango": 8, "Cherry": 5},
    103: {"Apple": 10}
}

def combine_values(input_dict):
    combined_dict = {}

    for sub_dict in input_dict.values():
        for key, value in sub_dict.items():
            if key in combined_dict:
                combined_dict[key] += value
            else:
                combined_dict[key] = value

    return combined_dict

# Combine values from dict1 into dict2
dict2 = combine_values(dict1)

# Print the resulting dictionary
print("Dict2 =", dict2)