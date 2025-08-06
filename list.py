my_list =[10,20,30,40]
my_list.insert(1,15)
new_list =[50,60,70]
my_list.extend(new_list)
my_list.remove(70)
my_list.sort(reverse= False)
print(my_list)
index= my_list.index(30)
print("The index of 30 is:",index)
