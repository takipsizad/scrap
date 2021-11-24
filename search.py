import os,tarfile
import re
os.chdir("tgz")
regex = "[A-Za-z\d]{23}\.[\w-]{6}\.[\w-]{27}/g"
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        fi = os.path.join(root, name)
        f = tarfile.open(name, "r")
        for tarinfo in f.getmembers():
            if  tarinfo.isfile() == True:
                file=f.extractfile(tarinfo)
                content = file.read()
                if re.search(regex,str(content)):
                    print(re.search(regex,str(content)))
    #for name in dirs:
    #    print(os.path.join(root, name))
    