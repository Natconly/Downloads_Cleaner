#Automation to sort downloads folder into relevent folders
import os, shutil

# Need to have the code access the downloads folder
path = os.chdir('../Downloads')
downloads_list = os.listdir(path)

# print(downloads_list)

#test moving a documnet
# shutil.move("/Users/nathans/Downloads/katho.jpg", "/Users/nathans/Documents/Downloads_Cleanup/photos/")

# Loop through each file and determine a "type", ie photo, pdf, misc
for file in downloads_list:
    try:                #if else structure to move files
        if file == photos:
            shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/photos/" + file)
        elif file == printer:
            shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/printer/" + file)
        elif file == pdf:
            shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/pdf/" + file)
        elif file == installers:
            shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/installers/" + file)
        elif file == code:
            shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/code/" + file)
        elif file == data:
            shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/data/" + file)
    except:
        shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/other/" + file)
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