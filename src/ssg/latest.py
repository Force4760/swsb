import os
import re
import src.ssg.meta as meta

def get_files(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    files = os.listdir(dirName)
    all_files = []
    # Iterate over all the entries
    for entry in files:
        # Create full path
        full_path = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(full_path):
            inner_files = get_files(full_path)
            for file in inner_files:
                all_files.append(file)
        else:
           all_files.append(full_path)
                
    return all_files


def latest(dirName):
    files = get_files(dirName)
    real_files=[]
    for f in files:
        print(f)
        if f[-3:] != ".md":
            files.remove(f)
    print(files)

    latest_file = max(files, key=os.path.getctime)
    me = meta.get_meta(latest_file)
    print(latest_file)
    latest_file=latest_file.replace("src/pages", "pages")
    latest_file=latest_file.replace(".md", ".html")
    print(latest_file)
    return [latest_file, me]