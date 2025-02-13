list1=[10,20,30,10,20,40,10]
counted=[]
for i in range(len(list1)):
        if list1[i] not in counted:
            count = 0
            for j in range(len(list1)):
                if list1[i] == list1[j]:
                    count += 1
            print(f"{list1[i]}: {count}")
            counted.append(list1[i]) 