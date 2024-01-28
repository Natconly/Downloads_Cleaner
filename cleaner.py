#Automation to sort downloads folder into relevent folders
import os, shutil, time

#start the time function to track duration
start = time.time()

# Need to have the code access the downloads folder
path = "/Users/nathans/Downloads/"
downloads_list = os.listdir(path)

#lists of file types and counters
photos = [".png", ".jpg", ".jpeg", ".heic"]
photo_count = 0
printer = [".stl", "obj.", ".3mf"]
printer_count = 0
pdf = [".pdf"]
pdf_count = 0
installers = [".dmg", ".iso", ".zip"]
installer_count = 0
code = [".py", ".mg"]
code_count = 0
data = [".exe", ".csv",".pptx"]
data_count = 0
other_count = 0

#test moving a documnet
# shutil.move("/Users/nathans/Downloads/katho.jpg", "/Users/nathans/Documents/Downloads_Cleanup/photos/")

# Check that destination locations exist, if not, create them.
if os.path.exists("/Users/nathans/Documents/Downloads_Cleanup/photos/") == False:
    os.makedirs("/Users/nathans/Documents/Downloads_Cleanup/photos/")
if os.path.exists("/Users/nathans/Documents/Downloads_Cleanup/printer/") == False:
    os.mkdir("/Users/nathans/Documents/Downloads_Cleanup/printer/")
if os.path.exists("/Users/nathans/Documents/Downloads_Cleanup/pdf/") == False:
    os.mkdir("/Users/nathans/Documents/Downloads_Cleanup/pdf/")
if os.path.exists("/Users/nathans/Documents/Downloads_Cleanup/installers/") == False:
    os.mkdir("/Users/nathans/Documents/Downloads_Cleanup/installers/")
if os.path.exists("/Users/nathans/Documents/Downloads_Cleanup/code/") == False:
    os.mkdir("/Users/nathans/Documents/Downloads_Cleanup/code/")
if os.path.exists("/Users/nathans/Documents/Downloads_Cleanup/data/") == False:
    os.mkdir("/Users/nathans/Documents/Downloads_Cleanup/data/")
if os.path.exists("/Users/nathans/Documents/Downloads_Cleanup/other/") == False:
    os.mkdir("/Users/nathans/Documents/Downloads_Cleanup/other/")

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
        photo_count += 1
    elif file_type in printer:
        shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/printer/" + file)
        printer_count += 1
    elif file_type in pdf:
        shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/pdf/" + file)
        pdf_count += 1
    elif file_type in installers:
        shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/installers/" + file)
        installer_count += 1
    elif file_type in code:
        shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/code/" + file)
        code_count += 1
    elif file_type in data:
        shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/data/" + file)
        data_count += 1
    else:
        shutil.move(path + file, "/Users/nathans/Documents/Downloads_Cleanup/other/" + file)
        other_count += 1

end = time.time()
print("\nFinished! All files successfully moved.\nExecution time of the program is", end - start, "\n",photo_count," Photo files moved\n", printer_count," Print files moved\n", pdf_count," PDF files moved\n", installer_count," Installation files moved\n", code_count," Code files moved\n", data_count," Data files moved\n", other_count," Other files moved")

""" *******  Notes *******
os.path.exists() - verifys that a file/directory location actually exists
"""