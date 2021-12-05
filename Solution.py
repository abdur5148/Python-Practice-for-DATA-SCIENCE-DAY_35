var1 = tuple([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
list1 = list()
for i in var1:
    if i % 2 == 0:
        list1.append(i)
t1 = tuple(list1)
print(t1)
