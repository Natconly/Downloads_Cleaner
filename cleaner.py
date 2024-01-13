#Automation to sort downloads folder into relevent folders
import os, shutil, time

#start the time function to track duration
start = time.time()

# Need to have the code access the downloads folder
path = "/Users/nathans/Downloads/"
downloads_list = os.listdir(path)

#list of file types and destination folders
photos = [".png", ".jpg", ".jpeg", ".heic"]
printer = [".stl", "obj.", ".3mf"]
pdf = [".pdf"]
installers = [".dmg", ".iso", ".zip"]
code = [".py", ".mg"]
data = [".exe", ".csv",".pptx"]

#test moving a documnet
# shutil.move("/Users/nathans/Downloads/katho.jpg", "/Users/nathans/Documents/Downloads_Cleanup/photos/")

# Loop through each file and determine a "type", ie photo, pdf, misc
for file in downloads_list:
    file_type = None
    for length in range(3, 6):
        if file[-length] == ".":
            file_type = file[-length:]
            break
    # print(file_type)
        
                   #if else structure to move files
    if file_type in photos:
        shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/photos/" + file)
    elif file_type in printer:
        shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/printer/" + file)
    elif file_type in pdf:
        shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/pdf/" + file)
    elif file_type in installers:
        shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/installers/" + file)
    elif file_type in code:
        shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/code/" + file)
    elif file_type in data:
        shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/data/" + file)
    else:
        shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/other/" + file)

end = time.time()
print("Finished! All files successfully moved.\n Execution time of the program is", end - start)

""" *******  Notes *******
os.path.exists() - verifys that a file/directory location actually exists
"""