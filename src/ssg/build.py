import topic 
import index 
import posts 
import os
import functions 
from subprocess import call

functions.rm("build")
index.index()
topic.top()
posts.make_posts()
functions.cp_dir("src/templates/images", "build/images")
functions.cp_dir("src/templates/css", "build/css")
functions.cp_dir("src/templates/fonts", "build/fonts")