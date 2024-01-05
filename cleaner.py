#Automation to sort downloads folder into relevent folders
import os, shutil

# Need to have the code access the downloads folder
path = os.chdir('../Downloads')
downloads_list = os.listdir(path)

#list of file types and destination folders
photos = [".png", ".jpg", ".jpeg", ".heic"]
printer = [".stl", "obj.", ".3mf"]
pdf = [".pdf"]
installers = [".dmg", ".iso"]
code = [".py", ".mg"]
data = [".exe", ".csv",".pptx"]
# print(downloads_list)

#test moving a documnet
# shutil.move("/Users/nathans/Downloads/katho.jpg", "/Users/nathans/Documents/Downloads_Cleanup/photos/")

# Loop through each file and determine a "type", ie photo, pdf, misc
for file in downloads_list: 
    file3 = file[-3:]
    file4 = file[-4:]
    file5 = file[-5:]
    print (file3, file4)
    if "." ==file3[:1]:
        file_type = file3
    elif"." ==file4[:1]:
        file_type = file4
    elif"." ==file5[:1]:
        file_type = file5

    # try:                #if else structure to move files
    #     if file in photos:
    #         shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/photos/" + file)
    #     elif file in printer:
    #         shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/printer/" + file)
    #     elif file in pdf:
    #         shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/pdf/" + file)
    #     elif file in installers:
    #         shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/installers/" + file)
    #     elif file in code:
    #         shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/code/" + file)
    #     elif file in data:
    #         shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/data/" + file)
    # except:
    #     shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/other/" + file)
    # if os.path.isfile(file):
    #     print(file)
  



""" *******  Notes *******
os.path.exists() - verifys that a file/directory location actually exists
"""