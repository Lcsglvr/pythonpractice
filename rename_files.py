#rename_files.py
#by Dr Lcsglvr 3-6-2018


#deleting the numbers from all file names in single directory; e.g., 5johny222.txt-> johny.txt

#this imports the necessary module (os) and defines the function
import os
def rename_files():

#get the file list in the directory you want to rename the files
    filelist=os.listdir(r"C:\Users\bleep\Desktop\random")
    print(filelist)
    savedpath=os.getcwd()
    print("Current Working Directory is: "+savedpath)

#this changes the current working directory to the one you want to rename files
    os.chdir(r"C:\Users\bleep\Desktop\random")

#this loops around to every file, such that it prints its old name, strips it of the numbers,
#and prints its new name
    for file_name in filelist:
        print("Old file name is "+file_name)
        print("New file name is "+file_name.translate(None, "0123456789"))
#changes back to the original working directory
        os.chdir(savedpath)

#this ends the function
rename_files()      
