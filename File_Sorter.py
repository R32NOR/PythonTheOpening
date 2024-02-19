# WELCOME TO File_Sorter!
# This script will sort all the files in the catalogue you will choose into few categories.

''' Below in dictionary named: "fileTypesDict" you can check what categories are predefined and what file extensions
are assigned to each category.
Feel free to add own categories or file extensions or move file extensions to other category.
fileTypesDict.keys() are for the category names
fileTypesDict.values() are for file extensions that are assigned to this category '''

# !!!ATTENTION!!!
# If there is directory named by the category (fe. if you used this script before) there is file with the same name
# in category (destination) directory, it will be overwritten!!!

# above will be upgraded in the future to choose what to do in such conflict, but now this script is just for my training.
# it will be also upgrade with log file with the data and history of using.
# ... someday :)

# Bon apetit! | 2024 | R32NOR | anklebiters


import os
import shutil

path = input('drop the directory path that you want to sort: ')


def file_list_receiver(directory):
    """
    FUNCTION: returns list with all filenames in chosen directory
    :param directory: directory path where files have to be sorted
    :return fileList: list of files in chosen directory (that are not folders)
    """
    fileList = []  # Initialize empty list to store the file names:

    # below func iterates trough each file in dir- checking whether filename is a file (not a directory)
    # add file to the fileList if it is a file:
    for fileName in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, fileName)):
            fileList.append(fileName)
    return fileList  # Returns list of files


def file_category(fileExtension):
    """
    FUNCTION: returns the category of file
    :param fileExtension: file extension (without dot!)
    :return fileCategory: category of file defined in fileTypesDict.keys() that corresponds to fileExtension parameter.
    """
    # declaring groups of file types
    fileTypesDict = {
        'Images': ['png', 'jpg', 'bmp', 'gif'],
        'PDF': ['pdf'],
        'Docs': ['doc', 'docx', 'xls', 'xlsx', 'txt', 'ppt', 'pptx', 'odt'],
        'Music': ['mp3', 'wav'],
        'Video': ['mp4'],
        'Archive': ['rar', 'zip', '7z']
    }
    # loop that returns the category of file
    for filetype in fileTypesDict.values():
        if fileExtension.lower() in filetype:
            fileCategory = list(fileTypesDict.keys())[list(fileTypesDict.values()).index(
                filetype)]  # returns category name by searching the list with file extensions
            return fileCategory
        else:
            continue
    else:
        fileCategory = 'Other'
    return fileCategory


def create_category_dir(directory, fileCategory):
    """
    FUNCTION: creates category directory (if it does not exist)
    :param directory: directory path where files have to be sorted
    :param fileCategory: Category of file- defined in func. file_category()
    """
    finalDir = os.path.join(directory, fileCategory)  # dirPath for current category
    if not os.path.exists(finalDir):
        os.makedirs(finalDir)  # creates category directory if it doesn't exist


def send_file_to_category_dir(dirPath, fileName, fileCategory):
    """
    FUNCTION: send file to appropriate category dir
    :param dirPath: directory path where files have to be sorted
    :param fileName: filename with file extension
    :param fileCategory: Category of file- defined in func. file_category()
    """
    sourceFilePath = os.path.join(dirPath, fileName)  # chosen file path
    destinationDirectoryPath = os.path.join(dirPath, fileCategory, fileName)  # destination folder
    shutil.move(sourceFilePath, destinationDirectoryPath)  # sends file to destination folder


def file_sorter(path):
    """
    FUNCTION: main function- that sort files in chosen directory and deliver them to appropriate category dir
    :parameter path: path to the directory and list of files
    """

    listOfFiles = file_list_receiver(path)  # gets list of files by running func: file_list_receiver
    fileExt = ''  # variable that will contain file extension retrieved in below loop

    # looping within list of files to sort each file:
    for file in listOfFiles:

        fileNameLength = len(file)
        dotFromBack = 1
        # below loop gets the extension of file
        for dotFromBack in range(1, fileNameLength):
            if file[dotFromBack * (-1)] != '.':
                dotFromBack += 1
            else:
                dotPosition = fileNameLength - dotFromBack
                fileExt = file[dotPosition + 1:]  # here we get the extension of current file
                fileCategory = file_category(
                    fileExt)  # now script checks the category of file by using function: file_category()
                create_category_dir(path,
                                    fileCategory)  # creates category dir (if it doesn't exist) with f. create_category_dir()
                send_file_to_category_dir(path, file, fileCategory)  # sending file to appropriate folder
                break  # exits the current loop and takes next file


file_sorter(path)  # starts sorting fuction
