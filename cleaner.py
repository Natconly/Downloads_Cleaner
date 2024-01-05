#Automation to sort downloads folder into relevent folders
import os, shutil

# Need to have the code access the downloads folder
path = os.chdir('../Downloads')
downloads_list = os.listdir(path)
# print(downloads_list)

# Loop through each file and determine a "type", ie photo, pdf, misc
for file in downloads_list:
    try:                #if else structure to move files
        if file == photos:
            shutil(source path, /Users/nathans/Documents/Downloads_Cleanup/photos/)
        elif file == printer:
            shutil(source path, /Users/nathans/Documents/Downloads_Cleanup/printer/)
        elif file == pdf:
            shutil(source path, /Users/nathans/Documents/Downloads_Cleanup/pdf/)
        elif file == installers:
            shutil(source path, /Users/nathans/Documents/Downloads_Cleanup/installers/)
        elif file == code:
            shutil(source path, /Users/nathans/Documents/Downloads_Cleanup/code/)
        elif file == data:
            shutil(source path, /Users/nathans/Documents/Downloads_Cleanup/data/)
    except:
        shutil(source path, /Users/nathans/Documents/Downloads_Cleanup/data/)
    # if os.path.isfile(file):
    #     print(file)
  


#Once identified, move file
photos = [".png", ".jpg", ".jpeg", ".heic"]
printer = [".stl", "obj.", ".3mf"]
pdf = [".pdf"]
installers = [".dmg", ".iso"]
code = [".py", ".mg"]
data = [".exe", ".csv"]



""" *******  Notes *******
os.path.exists() - verifys that a file/directory location actually exists
"""