collection =[1, 2, 3, 4]
print(collection, type(collection))
#  type list

for i in collection:
    print("i=", i)

print('first element: ', collection[0])
print('element -2: ', collection[-2])
print('len=', len(collection))

collection[2] = 234
collection.append(23423)
print(collection)

# Erease second element
collection.pop() # jesli puste to domyslnie jest -1 czyli ostatni
print(collection)


collection.pop(2)
print(collection)