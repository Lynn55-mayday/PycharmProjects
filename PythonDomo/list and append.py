name_list=['xiaoming','xiaohong','xiaolan']
print('---the temporary list before adding---')
for temp in name_list:
    print(temp)
temp_name=input("please enter a new name:")
name_list.append(temp_name)
print('---the list updated---')
for temp in name_list:
    print(temp)