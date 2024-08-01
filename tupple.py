menu = ('t','g','r','f')
print(type(menu))
print(len(menu))
print(menu)

menu1 = ('Tuple'+' '+'tyghh')
print(menu1) #not a tuple

menu2 = tuple(('tstt', 2545554, False)) # Tuple can store any of data type "you declear with a tuple constractor(Remember tuple constractor declear always with ()<--.)"
print(type(menu2))

# Tuple Access
menu3 = ('Shibu', "Rivu", "Shanti", 'Shiv')

print(menu3[3]) # you can access any index number

for x in menu3:
    print(x[0]) # each letter you can access

if 'a' in menu3[2]: # check if "a" in the index no 2....even you can check everything!.
    print('yes, you are right')



# Tuples are immutable or unchangable as you know but there is a workround. #####
# You can convert a tuple to a list and then you can change the list and then convert that list to a tuple. See below.####
menu4 = ('Rahul', 'Sajal', 'Barun')
menu5 = list(menu4)
menu5.append('Ratan')
menu4 = tuple(menu5)
print(menu4)

# You can also this######
menu6 = ('Tuple0', 'Tuple1', 'Tuple2')
menu7 = ('Tuple3',) # But remember when you creating only one item in a tuple it should be with a comma ","....
menu6 += menu7
print(menu6)


# You can remove item from tuple#

menu8 = ('remove', 'add', 'pluged', 'clear')
menu9 = list(menu8)
menu9.remove('remove')
menu8 = tuple(menu9)
print(menu8) # as you can "remove" item remove from the tuple.... 


# Unpack a tuple=====/
menu10 = ('ftfggr', 'book', 'pen','pencil')
# (red, green, blue) = menu10 # you get an error with this
(red, green, *blue) = menu10 # when you use asterisk(*) you get your result
blue.append('kala') # you can add value in a tuple....
print(green)
print(red)
print(blue)

