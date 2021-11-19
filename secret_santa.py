import random
file_name = input("file name: ")
file = open(file_name,'w')
names = {}
hat = []
print('Welcome to Secret Santa!')
new = input('Enter a name: ')
while new != '':
    names[new]=new
    hat.append(new)
    new = input('Next name: ')

for k in names:
    choose = random.choice(hat)
    while  choose == k:
        choose = random.choice(hat)
    names[k] = choose
    hat.remove(choose)

print("All done!")

for k , v in names.items():
    file.write(k+': '+v+'\n')
file.close()

input("Bye!")


