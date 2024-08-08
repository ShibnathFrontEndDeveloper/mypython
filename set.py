# set alwaya declear by "{}"<---!

menu0 = {'Fruits', 'Chocolate', 'Drink', 'Chocolate'}
for x in menu0:
    print(x)


menu1 = {'Add', 'Remove', 'Clear', 'Append', 'Count'}
menu1.add('Copy') #You can Add item in the set....
for x in menu1:
    print(x)


menu2 ={1,2,3,4,5}
menu3 = {'Add', 'Remove', 'Clear', 'Append', 'Count'}
menu3.add('Append')
menu2.update(menu3) #use update method for added
print(menu2)


# Remove set item

menu4 = {"Added", "List", "Menu", "Accordion"}
x = menu4.pop() # pop method remove random one item from set....
print(x)
print(menu4)

menu5 = {'Akila', 'Sakila', 'Nakila'}
menu5.discard('Akila') # remove set item by discard() or remove() Method....
menu5.remove('Sakila')
print(menu5)

# set join method use union() method or | <---method.....

menu6 = {'Akila', 'Sakila', 'Nakila'}
menu7 = {"Added", "List", "Menu", "Accordion"}
menu8 = menu6.union(menu7)
print(menu8)
print(len(menu8))


print()

menu6 = {'Akila', 'Sakila', 'Nakila'}
menu7 = {"Added", "List", "Menu", "Accordion"}
menu9 = menu6 | menu7
print(menu9)


# Set Methods=======/
menu10 = {'Pagla', 'Tagla', 'Nagla','Chhagla'}
menu10.add('Takla')
print(menu10)

menu11 = {'Company', 'House', 'Room'}
menu12 = {'Road', 'Tree', 'House'}
menu14 = {'Fuit', 'Water', 'Wind'}

menu13 = menu12.difference_update(menu11,menu14)
print(menu13)

menu13 = menu12 - menu11 - menu14
print(menu13)


menu15 = {5, 50, 100, 200}
menu15.discard(200)
print(menu15)