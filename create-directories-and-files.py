import os

fileTotal = 9 # number of files to be created
newDirectory = "folder-name"
fileName = "file-name"
rootDirectory = r"C:\path\to\directory" # the location where the folder and files will be created
extension = "html" # the file extension for each file e.g. txt, html, js, py etc...

try:
    path = os.path.join(rootDirectory, newDirectory)
    os.mkdir(path)

    for i in range(1, fileTotal + 1):
        zero = '0' if i < 10 else '' # place a zero before single digits so that the folder orders the files correctly
        open(rf"{rootDirectory}\{newDirectory}\{zero}{i}{fileName}.{extension}", "x")
except FileExistsError as err:
    print(err)
except FileNotFoundError as err:
    print(err)
else:
    print('directory and files created')
