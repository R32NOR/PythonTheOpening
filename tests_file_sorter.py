fileExtension='mp4'

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








