import os

def list_deep_files(folder_path):
    deep_files = []
    #function returns a list of all the files and directories contained in a given directory.
    #list only contains the file names not the whole path
    for filename in os.listdir(folder_path):
        if filename.startswith('deep'):
            # the whole path is added to the file
            filepath = os.path.join(folder_path, filename)
            deep_files.append(filepath)
    return deep_files