from pytube import YouTube
import re
import os
downloads = "Music"


def rename(text):
    chars = "/|\.\"',; "
    for c in chars:
        text = text.replace(c, "_")
    return text

def download_one(link,name, downloads, msg = ""):
    name = rename(name)
    try:
        yt = YouTube(link)
    except:
        print("Connection Error!")
    try:
        print("Downloading...", msg)
        
        if not os.path.isfile(os.path.join(downloads, name)+".mp3"):
            v = yt.streams.filter(only_audio=True)
            v[0].download(downloads, filename = name)
            os.rename(os.path.join(downloads, name)+".mp4",os.path.join(downloads, name)+".mp3")
            print("Download completed!")
        else:
            print("Already Downloaded!")
        
    except:
        print("Error!")

def get_songs(file):
    with open(file, "r") as f:
        text = f.read()
    return re.findall(r"\[(.*)\]\((.*)\)", text)

def download(file, downloads, name):
    name = rename(name)
    songs = get_songs(file)
    downloads = os.path.join(downloads, name)
    max = len(songs)
    i = 1
    for song in songs:
        msg = f"[{i}/{max}]"
        download_one(song[1],song[0], downloads, msg = msg)
        i += 1



if __name__ == "__main__":
    os.system('clear')
    name = input("Name: ")
    file = input("File (src/pages/.../...): ")
    file = os.path.join("src/pages", file)
    download(file, downloads, name)