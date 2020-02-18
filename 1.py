import os
print("Enter your path: ")  #/Users/Шкимишки/Documents/Work2/folder1/
Path = input()
os.chdir(Path)
print(os.getcwd())

def FirstMenu():
    print('''Enter "1" in order to open Directory manage options
Enter "2" in order to open File manage options
Enter "3" If you want to end this program''')

def ManagerforDir():
    print('''Directory manage options:
1) rename directory
2) print number of files and directories in it
3) list content of the directory 
4) add file to this directory
5) add new directory to this directory
6) back to Main Menu''') 
    innum=int(input())
    if innum==1:
        print('Please enter old name of the directory: ')
        oldname=input()
        print('Please enter new name of the directory: ')
        newname=input()
        os.rename(oldname, newname)
        print("The name of the directory has changed")
    elif innum==2:
        filecnt=0
        dircnt=0
        for root, dirs, files in os.walk(Path):
            for directories in Path:
                dircnt=dircnt+1
            for files in Path:
                filecnt= filecnt + 1
        print("The number of files: ", filecnt)
        print("The number of directories: ", dircnt)
    elif innum==3:
        print('The content of this directory:')
        print(os.listdir(Path))
    elif innum==4:
        print('Enter the name of new file: ')
        newname=input()
        filee = open(newname, 'w')
        filee.close()
        print('The new file has created')
    elif innum==5:
        print('Enter the name of the new directory:')
        newname=input()
        os.mkdir(newname)
        print("The new directory has created")
    elif innum==6:
        exist=True

def ManagerforFile():
    print('''File manage options:
1) delete file
2) rename file
3) add content to this file
4) rewrite content of this file
5) return to the parent directory
6) back to Main Menu''')
    innum=int(input())
    if innum==1:
        print('Enter the full name of file:')
        fname=input()
        os.remove(fname)
        print("This file was deleted")
    elif innum==2:
        print('Please enter old name of the file with the extension: ')
        oldname=input()
        print('Please enter new name of the file with the extension: ')
        newname=input()
        os.rename(oldname, newname)
        print("The name of the file has changed")
    elif innum==3:
        print('Enter the name of the file with the extension: ')
        fname=input()
        filee = open(fname, 'a')
        print("Enter the content that you want to add to this file: ")
        fcontent=input()
        filee.write(fcontent)
        filee.close()
        print("The content has added to this file")
    elif innum==4:
        print('Enter the name of the file with the extension: ')
        fname=input()
        filee = open(fname, 'w')
        print("Enter the content that will replace previous content: ")
        fcontent=input()
        filee.write(fcontent)
        filee.close()
        print("The content was rewritten")
    elif innum==5:
        os.chdir(Path)
        print(os.getcwd())
    elif innum==6:
        exist=True 

exist=True

while exist:
    FirstMenu()
    innum=int(input())
    if innum==1:
        ManagerforDir()
    elif innum==2:
        ManagerforFile()
    elif innum==3:
        print('This program is ended')
        exist=False