import os
import parser
import re
import functions

def make_posts():
    topics = [ f.path for f in os.scandir("src/pages") if f.is_dir() ]
    with open("src/templates/blog.html", "r") as template:
        t = template.read()
    for topic in topics:
        posts = os.listdir(topic)
        build = topic.replace("src", "build")
        functions.cp_dir(topic + "/assets", build)
        for post in posts:
            if post[-3:] == ".md" and not os.path.isdir(post):
                with open(f"{topic}/{post}", "r") as p:
                    content = parser.parser(p.read(), f"{topic}/{post}")
                    title = content[0][0].replace("_", " ")
                    t1 = re.sub("\<\!\-\-Title\-\-\>", title, t)
                    t1 = re.sub("\<\!\-\-Author\-\-\>", content[0][1], t1)
                    t1 = re.sub("\<\!\-\-Date\-\-\>", content[0][2], t1)
                    t1 = re.sub("\<\!\-\-Content\-\-\>", content[1], t1)
                    
                with open(f"{build}/{post[:-3]}.html", "w") as f:
                    f.write(t1)