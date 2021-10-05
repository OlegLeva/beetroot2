with open('myfile.txt', 'w') as my_file:
    my_file.write("Hello file world!\n")

with open('myfile.txt') as my_file:
    r = my_file.read()
print(r)

with open('myfile.txt', 'a') as my_file:
    my_file.write("Hello world!\n")

with open('myfile.txt') as my_file:
    r = my_file.read()
print(r)
