import os

def processFilePath(file_path: str):
    file_name = os.path.split(file_path)[1]
    file_name, file_extension = getFileExtension(file_name)
    file_name, file_part_idx = getFilePartIdx(file_name)
    return file_name, file_extension, file_part_idx
    

def getFileExtension(file_name: str):
        if '.' in file_name:
            return tuple(file_name.split('.', 1))
        return file_name, None

def getFilePartIdx(file_name: str):
    try:
        file_part = file_name.rsplit('_', 1)[1]
        file_part = 0 if file_part == 'a' else 1
        return file_name[:-2], file_part
    except:
        raise ValueError(f'could not parse file part index! in file \'{file_name}\'')
