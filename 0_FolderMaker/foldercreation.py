import os


def create_folder(folder_name):
    try: 
        filename = ""
        filename = folder_name[folder_name.find("_")+1:]
        
        path = os.path.join(os.getcwd(), folder_name)
        os.makedirs(path)
        
        file_path = path +"/" +  filename + ".py"
        
        with open(file_path,"w") as file:
            file.write("print('hello world')\n")
        
        print(f'path {file_path} created')
        
    except FileExistsError:
        print("Folder {folder_name} already exists")
        
        


# get file full of folder names
os.listdir()

file = open("0_FolderMaker/Folderlist.txt","r")
folder = []
for x in file.readlines():
    # convert to correct format
    splitx = x.split(" ")
    newx = " "
    newx += '_'.join(splitx)
    strippedx = newx.rstrip()
    # convert to list
    folder.append(strippedx)

for x in folder:
    #pass to folder creator
    create_folder(x)