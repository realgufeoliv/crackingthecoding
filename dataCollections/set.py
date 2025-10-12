# set is a data collection that is unchangeable, unordered, unindexed and not allow duplicates

# Access Item: is not possible to access a item with key or index. but you can loop using for
print("\nGETTING ITEMS")
thisset = {"Apple", "Banana", "Cherry"}
for fruit in thisset:
    print(fruit)
print("\n")

# or you can use in
print("CHECKING ITEMS")
print("Banana" in thisset)
print("Apple" not in thisset)

# add element with add method
print("\nADDING ITEM")
thisset.add("orange")
print(thisset)
print("\n")
print("ADDING ANOTHER SETS")

# add another set with method update (IT'S POSSIBLE TO ANY ITERABLE  )
anotherset = {"a", "b", "c"}
thisset.update(anotherset)
print(thisset)
thisset.update(["lion", "dog", "cat"])
print(thisset)

# Discard and Remove methods (The difference is that if the item doesn't exists remove will raise an error and discard no)
print("\nDiscard and Remove Items")
thisset.remove("lion")
thisset.discard('Banana')
print(thisset)

#pop() method will remove a random item of the set and return this item
print('\n POP ITEM')
item_x = thisset.pop()
print(item_x)
print(thisset)

#clear() method remove all element from set
print('\n Clear set')
thisset.clear()
print(thisset)

#clear() method remove all element from set
print('\n Del set')
del anotherset
#print(anotherset) it will raise an error

