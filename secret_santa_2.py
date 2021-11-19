file_name = input("file name: ")
file = open(file_name,'r')
search = input("Enter your name to see who you got: ")
for line in file:
    if line.split(':')[0].lower()== search.lower():
        print(line)

file.close()

input("Bye!")