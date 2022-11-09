def processFilePath(filePath: str):
    file_name = filePath.rpartition('/')[2]
    file_name, file_extension = getFileExtension(file_name)
    file_name, file_part_idx = getFilePartIdx(file_name)
    return file_name, file_extension, file_part_idx
    

def getFileExtension(file_name: str):
    if '.' in file_name:
        return tuple(file_name.split('.', 1))
    return file_name, None

def getFilePartIdx(file_name: str):
    file_part = file_name.rsplit('_', 1)[1]
    file_part = 0 if file_part == 'a' else 1
    return file_name[:-2], file_part
