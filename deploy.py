import os.path
import os
from distutils import dir_util
import getpass

USERNAME = "yoavram"
BUILD_FOLDER = "/workspace/msb/build/"
DEPLOY_FOLDER = "/workspace/"+USERNAME+".bitbucket.org"
COMMIT_MESSAGE = "update"
DEBUG = False

def run_and_print(cmd):
    if DEBUG:
        print cmd
    else:
        fin = os.popen(cmd)
        print fin.read()
        fin.close()

import sitebuilder
sitebuilder.freeze()

os.chdir(DEPLOY_FOLDER)
print "cd",os.getcwd()
run_and_print("hg pull")
copied_files = dir_util.copy_tree(BUILD_FOLDER,".")
print "Copied",len(copied_files),"files"
# hg merge?
run_and_print('hg add *')
run_and_print('hg commit -m "'+COMMIT_MESSAGE+'"')
passwd = getpass.getpass()
run_and_print("hg push https://"+USERNAME+":"+passwd+"@bitbucket.org/"+USERNAME+"/"+USERNAME+".bitbucket.org")
