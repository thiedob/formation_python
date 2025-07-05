"""#os managment with python
import os
chemin = os.getcwd()
print("Current working directory:",chemin)

#changing directory
import os
def current_dir():
    print("Current working directory before")  
    print(os.getcwd())
    print( )

current_dir()
os.chdir("../")
current_dir()

"""
#Directory creation using os.mkdir method
import os
"""
directory = "images"
parent_dir = "/home/thiedo/Desktop/formation_python"
path = os.path.join(parent_dir, directory)
os.mkdir(path)

print("Directory '% s' created", directory)

directory = "piece_jointe"
parent_dir = "/home/thiedo/Desktop/formation_python"
path = os.path.join(parent_dir, directory)
mode = 0o666

os.mkdir(path, mode)
print("Directory '% s' created", directory)


directory = "dossier_test"
parent_dir ="/home/thiedo/Desktop/formation_python"
path = os.path.join(parent_dir, directory)
os.makedirs(path)
print("Directory '% s' created" % directory)
directory = "c"
parent_dir = "D:/Pycharm projects/GeeksforGeeks/a/b"
mode = 0o666
path = os.path.join(parent_dir, directory)
os.makedirs(path, mode)
print("Directory '% s' created" % directory)

cwd = "/"
chemin = os.listdir(cwd)
print(chemin)

os.remove(path)     removes an file from given directory

or.rmdir(path)      removes an empty directory given in path description        

file = 'file.txt'
os.rename(file,'New.txt')       rename a given file name

os.path.exists('file.txt')       check weither a file exit or not

os.path.getsize('file.txt')       Return the size of a file 

"""