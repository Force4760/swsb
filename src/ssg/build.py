import src.ssg.topic as topic
import src.ssg.index as index
import src.ssg.posts as posts
import os
import src.ssg.functions as functions
from subprocess import call

functions.rm("build")
index.index()
topic.top()
posts.make_posts()
functions.cp_dir("src/templates/images", "build/images")
functions.cp_dir("src/templates/css", "build/css")
functions.cp_dir("src/templates/fonts", "build/fonts")