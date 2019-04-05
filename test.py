# IPython Writing a File
%%writefile test.txt
Hi, this is python world!!

#Open a File
file = open('test.txt')

#Read File
file.read()

#Seek to the start of file
file.seek(0)

#Readlines returns a list of the lines in the file
file.readlines()

#Writing to a File
file = open('test.txt','w+')
file.write('This is my territory')

#Appending to a File
file = open('test.txt','a+')
file.write('\nI can do anything I want.')

#Print a File
print(file.read())

