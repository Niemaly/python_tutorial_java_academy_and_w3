import platform
import w3schools.import_ex.person as p


array = dir(platform)

array2 = dir(p)
print(array2)

for i in array:
    print(i)