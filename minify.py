from calmjs.parse import es5, io
from calmjs.parse.unparsers.es5 import minify_print
from rcssmin import cssmin
import sys, os
path = sys.argv[1]
print(path)
for x in os.listdir(path):
    print(x)
    if not x.__contains__('.min.'):
        if x.endswith('.js'):
            js_file = open(path+"/"+x.split(".")[0]+".js")
            new_file = open(path+"/"+x.split(".")[0]+".min.js", 'w')
            new_file.write(minify_print(io.read(es5, js_file), obfuscate=True)) 
            new_file.close()
            js_file.close()
        if x.endswith('.css'):
            css_file = open(path+"/"+x.split(".")[0]+".css")
            new_file = open(path+"/"+x.split(".")[0]+".min.css", "w")
            new_file.write(cssmin(css_file.read(), keep_bang_comments=False))
            new_file.close()
            css_file.close()
