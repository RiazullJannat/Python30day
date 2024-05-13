f = open("doc.txt", "r")
for i in f:
    print(i)


with open('doc.txt','r') as file:
    print(file.read())

with open('test.txt','w') as wf:
    wf.write('The quick brown fox jumps over the lazy dog.')

with open('doc.txt', 'r') as rf:
    print(rf.read(5))

    print()

with open('doc.txt', 'r') as rrr:
    #print(rrr.readline())
    print(rrr.readlines())

file = open('test.txt','w')
file.write('This is the write command.\n')
file.write("It allows us to write in a particular file.\n")
file.close()

with open('test.txt', 'a') as a:
    a.write('This will append this line.')


# Implementing all the functions in file handling
import os
def create_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write('Hello, world!\n')
        print(f'file {filename} created successfully.')
    except IOError:
        print(f"Error: could not create file {filename}")


def read_file(filename):
    try:
        with open(filename,'r') as f:
            content = f.read()
            print(content)
    except IOError:
        print(f"Error: could not read file {filename}")


def append_file(filename, txt):
    try:
        with open(filename, 'a') as a:
            a.write(txt)
        print(f'Text append to the file {filename} successfully.')
    except IOError:
        print(f'Error: could not append to the file {filename}')



def rename_file_name(filename, newname):
    try:
        os.rename(filename, newname)
        print(f"File {filename} renamed to {newname} successfully.")
    except IOError:
        print(f"Error: could not rename file {filename}.")



def delete_file(filename):
    try:
        os.remove(filename)
        print(f'File {filename} deleted successfully.')
    except IOError:
        print(f'Error: could not delete file {filename}')
if __name__ == '__main__':
    filename= 'rdox.txt'
    newname = 'rjdox.txt'
    create_file(filename)
    read_file(filename)
    append_file(filename,'Appending first time.')
    read_file(filename)
    rename_file_name(filename,newname)
    read_file(newname)
    delete_file(newname)