# jaka roznica pomiedzy () - read only a [] - mozna zmieniac
collection =(1, 2, 3, 4) # can not be changed
print(collection, type(collection))
#  type list

for i in collection:
    print("i=", i)

print('first element: ', collection[0])
print('element -2: ', collection[-2])
print('len=', len(collection))

# updating
collection[2]=333