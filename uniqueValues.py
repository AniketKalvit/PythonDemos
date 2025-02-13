d1=[{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, {'VII': 'S005'}, {'V': 'S009'},
{'VIII': 'S007'}]


unique_values=set()

for d in d1:
    for x in d.values():
        unique_values.add(x)

for i in unique_values:
    print(i)