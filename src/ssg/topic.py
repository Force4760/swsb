import os
import meta as meta
import re

def create_topics(folder):
    files = os.listdir(folder)
    for file in files:
        if file[-3:] != ".md":
            files.remove(file)
            
    def s(file):
        file = folder + file
        return os.path.getctime(file)
    files.sort(key=s)
    files.reverse()
    return files

def create_section(base, files):
    section = """"""
    for file in files:
        m = meta.get_meta(base + file)
        f = file.replace(".md",".html")
        section+=f"""
        <section class="content">
          <div class="bg-img" style="background: url({m[4]});"></div>

            <h2><a href="{f}">{m[0]}</a></h2>
            <p>{m[1]} - {m[2]}</p>
            <p>{m[3]}</p>
        </section>
        
        """
    return section


def top():
    topics = os.listdir("src/pages")
    with open("src/templates/topics.html", "r") as template:
        t = template.read()

    for topic in topics:
        t1 = t
        to_add = create_section(f"src/pages/{topic}/", create_topics(f"src/pages/{topic}/"))
       
        t1 = re.sub("\<\!\-\-Title\-\-\>", topic.replace("_", " ").capitalize(), t1)
        t1 = re.sub("\<\!\-\-Add Posts\-\-\>", to_add, t1)
        os.makedirs(f"build/pages/{topic}/", exist_ok=True)
        with open(f"build/pages/{topic}/posts.html", "w") as f:
            f.write(t1)