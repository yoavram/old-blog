import os.path
import os
from distutils import dir_util
import getpass
import sitebuilder

USERNAME = "yoavram"
BLOG_REPO = "msb"
BUILD_FOLDER = "/workspace/msb/build/"
DEPLOY_FOLDER = "/workspace/"+USERNAME+".bitbucket.org"
COMMIT_MESSAGE = "update"
DEBUG = False
PASSWORD = getpass.getpass("Bitbucket password:")

def run_and_print(cmd):
    if DEBUG:
        print cmd
    else:
        fin = os.popen(cmd)
        print fin.read()
        fin.close()


# build the static blog
sitebuilder.freeze(False)
# TODO check for errors

# push commits of the blog builder (no commiting!)
run_and_print("hg push https://"+USERNAME+":"+PASSWORD+"@bitbucket.org/"+USERNAME+"/"+BLOG_REPO)

# add, commit, push the static blog
os.chdir(DEPLOY_FOLDER)
print "cd",os.getcwd()
run_and_print("hg pull") # this is only done for the right cycle, it doesnt matter at all, so no update.
copied_files = dir_util.copy_tree(BUILD_FOLDER,".")
print "Copied",len(copied_files),"files"
# hg merge?
run_and_print('hg add .') 
run_and_print('hg commit -m "'+COMMIT_MESSAGE+'"')
run_and_print("hg push https://"+USERNAME+":"+PASSWORD+"@bitbucket.org/"+USERNAME+"/"+USERNAME+".bitbucket.org --force")
