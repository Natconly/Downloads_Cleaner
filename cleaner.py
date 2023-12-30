#Automation to sort downloads folder into relevent folders
import os

# Need to have the code access the downloads folder
path = os.chdir('../Downloads')
downloads_list = os.listdir(path)
print(downloads_list)

#Loop through each file and determine a "type", ie photo, pdf, misc



#Once identified, move file