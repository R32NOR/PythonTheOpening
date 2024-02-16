import os
import datetime
from typing import List

path=input('drop the directory path that you want to sort: ')


def file_list_receiver(directory):
    # Initialize empty list to store the file names:
    fileList=[]

    # iterate trough each file in dir
    for fileName in os.listdir(directory):
        # checking whether filename is a file (not a directory)
        if os.path.isfile(os.path.join(directory, fileName)):
            # add file to the list:
            fileList.append(fileName)

    return fileList

imageExtension= ['png', 'jpg', 'bmp', 'gif']
pdfExtension= ['pdf']
documentExtension= ['doc', 'docx', 'xsl', 'xslx', 'txt']
musicExtension = ['mp3', 'wav']
videoExtension = ['mp4']

newDirectories={'imageExtension': 'Images', 'pdfExtension': 'PDFs', 'documentExtension': "Docs", 'musicExtension': 'Music', 'videoExtension': 'Video'}



def file_sorter (directory, listOfFiles):

    fileExtensions=[]
    # taking each file in list of files
    for file in listOfFiles:
        # take extracted file list to get the file extension:

        dotPosition=int(len(file)-1)
        for dotPosition in range(0,len(file)):
            if file[dotPosition] != '.':
                dotPosition -= 1
            else:
                fileExt=file[dotPosition:]
                fileExtensions.append(fileExt)
    return print(fileExtensions)





files=file_list_receiver(path)
file_sorter(path, files)













