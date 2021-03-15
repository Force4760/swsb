import os
import re
import src.ssg.latest as latest

def index():
    filenames = os.listdir("src/pages")
    topics = []

    for file in filenames:
        if os.path.isdir("src/pages/" + file): # check whether the current object is a folder or not
            topics.append(file)

    t = """<ul>"""
    for topic in topics:
        topicname = topic.replace("_", " ").capitalize()
        t += f"""<li><a href="./pages/{topic}/posts.html">{topicname}</a></li>"""
    t+="</ul>"

    l = latest.latest("src/pages")
    l = f"""<a href="{l[0]}">{l[1][0]}</a>"""

    with open("src/templates/index.html", "r") as index:
        html = index.read()
        html = re.sub("\<\!\-\-Add Latest\-\-\>", l, html)
        html = re.sub("\<\!\-\-Add Topics\-\-\>", t, html)

    os.makedirs(f"build/", exist_ok=True)
    with open(f"build/index.html", "w") as f:
        f.write(html)