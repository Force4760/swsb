import re
def get_title(file):
    with open(file, "r") as f:
        title = re.findall("Title: (.*)", f.read())
    try:
        return title[0]
    except:
        return "No Title"
def get_author(file):
    with open(file, "r") as f:
        au = re.findall("Author: (.*)", f.read())
    try:
        return au[0]
    except:
        return "No Author"

def get_date(file):
    with open(file, "r") as f:
        date = re.findall("Date: (.*)", f.read())
    try:
        return date[0]
    except:
        return "No Date"
    
def get_img(file):
    with open(file, "r") as f:
        img = re.findall("(?:Img|Image): (.*)", f.read())
    try:
        return img[0]
    except:
        return ""

def get_overview(file):
    with open(file, "r") as f:
        img = re.findall("Overview: (.*)", f.read())
    try:
        return img[0]
    except:
        return "No Overview"

def get_meta(file):
    meta = []
    meta.append(get_title(file))
    meta.append(get_author(file))
    meta.append(get_date(file))
    meta.append(get_overview(file))
    meta.append(get_img(file))
    return meta


