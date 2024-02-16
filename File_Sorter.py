import os
import shutil

path=input('drop the directory path that you want to sort: ')

# Function that returns list with all filenames from chosen dir
def file_list_receiver(directory):
    # Initialize empty list to store the file names:
    fileList=[]

    # iterate trough each file in dir
    for fileName in os.listdir(directory):
        # checking whether filename is a file (not a directory)
        if os.path.isfile(os.path.join(directory, fileName)):
            # add file to the list:
            fileList.append(fileName)

    # As a return we get list of files in directory and are not a directories
    return fileList


# function that returns which category file is:
def file_category(fileExtension):

    # declaring groups of file types
    fileTypesDict = {
        'Images': ['png', 'jpg', 'bmp', 'gif'],
        'PDF': ['pdf'],
        'Docs': ['doc', 'docx', 'xls', 'xlsx', 'txt', 'ppt', 'pptx', 'odt'],
        'Music': ['mp3', 'wav'],
        'Video': ['mp4'],
        'Archive': ['rar', 'zip', '7z']
    }

    # loop that returns type of file
    for filetype in fileTypesDict.values():
        if fileExtension.lower() in filetype:
            fileCategory = list(fileTypesDict.keys())[list(fileTypesDict.values()).index(filetype)]
            return fileCategory
        else:
            continue
    else:
        fileCategory='Other'
    return fileCategory

#function that creates category directory (if it doesnot exist)
def create_category_dir(directory, fileCategory):
    finalDir=os.path.join(directory, fileCategory) # final directory for current file category

    if os.path.exists(finalDir)==True:
        return finalDir
    else:
        os.makedirs(finalDir)


# below we set function that we shuld input path to the directory and list of files
def file_sorter (directory, listOfFiles):
    fileExt=''  #variable that will contain file extension retrieved in below loop

    # taking each file in list of files
    for file in listOfFiles:
        # below we are looping for retrieving of file extension
         fileNameLength = len(file)
         dotFromBack = 1

         for dotFromBack in range(1,fileNameLength):
             if file[dotFromBack*(-1)] != '.':
                 dotFromBack += 1
             else:
                 dotPosition=fileNameLength-dotFromBack
                 fileExt = file[dotPosition+1:]
                 #print(file, fileExt)
                 fileCategory=file_category(fileExt)
                 create_category_dir(path,fileCategory)
                 sourceFilePath=os.path.join(path,file)
                 destinationDirectoryPath=os.path.join(path,fileCategory)
                 shutil.move(sourceFilePath, destinationDirectoryPath) # replace current file to final directory
                 break

# function call
files=file_list_receiver(path) # list of file that is returned from f. file_list_receiver

file_sorter(path, files)













