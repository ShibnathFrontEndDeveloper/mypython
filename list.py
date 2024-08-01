a = 45
b = 45
x = a*b
print(x)

a = 'Python is fabulous' # Global variable

def myPrint():
    a = "Python is good" # Local Variable
    print(a)

myPrint()
print(a)

a = {"Limba", "simba", "timba"} # set type data
b= {
    "limba":"Limba1",
    "Simba": "Simba1",
    "limba":"Shibu"
    }



print(a)
print(type(b))
print(b["limba"],["Simba"])


list = dict(name = 'Python', number = 45)

print(list)

myList = ['list', 'bisr', 'tist','jkukiiii','lkkiiiji','hgfftftyf', 'list'] #List data is changable....You remove data from here....
myList[1]='bist'
myList.remove('list')
b = myList.count('list')
# newList = list(('ljku', 'piku',150))

print(myList)
print(b)
print(len(myList))
print(myList[0:2])
myList[2] = "Folicia Albarto"  # Change the item value of index(2) means list data number 3 you can accesse all the items

if "filocona" and  "tist" in myList:
    print('you are ok! "tist" is there')
else:
    print('Sorry! not included')



print(myList)


secondList = [1,2,3,4,5,6,7,8,9,0]
for x in secondList:
    print(x)


thirdList = ['Shibnath', 'Shubhasish', 'Sukanta', 'Subrata']
for x in range(len(thirdList)):
    print(thirdList[x])

print()

for x in thirdList:
    print(x)

print()

i = 0
while i<len(thirdList):
    print(thirdList[i])
    i = i+1


menu = ['Book', 'Pen', 'Pencil']
[print(x) for x in menu]


print()

menu = ['list', 'sist', 'bist', 'tist']
menuComprehence= []

for x in menu:
    if 'i' in x:
        menuComprehence.append(x)
print(menuComprehence)

#for short line
print()
menu0 = ['list', 'sist', 'bist', 'tist']

meni01 = [x for x in menu0 if 'i' in x]
meni01.remove('bist')
meni01.append('Halolu') #or
meni01.insert(0, 'Kowalalu')

print(meni01)

# Extended list item method

m = [1,2,3,4,6,7]
l = ['Slohuu', 'Dgddgdglu', 'Topjlnlnhjk', 'Gffrfghj']
m.extend(l) # If aply the extened() then you will get result like [1,2,3,4,6,7,'Slohuu', 'dgddgdglu', 'topjlnlnhjk', 'gffrfghj'] this will appear with join....
print(m)
l.sort()
print(l)

m1 = ['list', 'tweest','sweets','tupple']
m1m = [x.upper() for x in m1]
m1m = [x if x != 'tweest' else 'bigwast' for x in m1]
print(m1m)


# Sort List Items=======/
m12m = ['sort', 'brot', 'tort', 'Frot', 'Kort', 'Gort']
m12m.sort(key= str.lower)
print(m12m)


def muDefFun(n):
    return abs(n<str())
m12m = ['sort', 'brot', 'tort', 'Frot', 'Kort', 'Gort']
m12m.sort(reverse= muDefFun)
print(m12m)

# You can make a copy of a list use by copy() method======/
menuCopy = ['copy1', 'copy2', 'copy3', 'copy4']
menuCopy1 = menuCopy.copy()
print(menuCopy1)





