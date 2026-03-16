# syntax
a = ['sedan','suv','trucks','suv']
b = ['classic','GTR']
print("Before: ",a)
# Accessing list items
""" print('index 0: ',a[0])
print('index 2: ',a[2])
print('index 1:4 :',a[1:4]) #slicing
print(" reversing: ",a[::-1])
print('last element: ',a[-1]) """

# Modify list
a[0]="Lorry"
print("After : ",a)
a.insert(2,"coupe")
for i,car in enumerate(a):
    a[i]=car.capitalize()

print("Updated : ",a)
# Add items
a.append("electric")
print("Append : ",a)
a.extend(b)
print("Extended : ",a)
# Remove items
a.remove("classic")
print("Remove : ",a)
a.pop(-2)
print("Pop : ",a)

# del a
# print("Delete : ",a)
# a.clear()
# print("Cleared : ",a)
# Looping through a list
# a.append("Hlse")
i=0
print("Length : ",len(a))
while i<len(a):
    print("{} : {}".format(i,a[i]))
    i=i+1
# list comprehension
for model in a:
    print("Model : ",model)

[print("List Comprehension : ",model) for model in a]

# sort lists
nums=[234,452,462,637,3,673,26,7,72,257,25254,723]
print("Before sort: ",nums)
nums.sort(reverse=True)
print("After Sort : ",nums)
print("A before sorting :",a)
a.sort()
print("A after sorting : ",a)


# copy lists
copyOfA=a.copy();

# join lists
c = a+b
print("C:",c)
#  Built in list methods

duplicate = a.count("Suv")
print("Count Suv : ",duplicate)