import os.path
import os
from distutils import dir_util
import getpass
import sitebuilder

DEBUG = True

REPO = "yoavram.github.com"
USERNAME = "yoavram"
SOURCE_BRANCH = "source"
BUILD_FOLDER = r"build/"
DEPLOY_FOLDER = r"../site/"
COMMIT_MESSAGE = "update"
USERNAME = "yoavram"
GIT_SERVER = "github.com"
PASSWORD = getpass.getpass("GitHub password:")

push_msg = "git push https://%s:%s@%s/%s/%s.git" % (USERNAME,PASSWORD,GIT_SERVER,USERNAME,REPO)


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
run_and_print(push_msg)

copied_files = dir_util.copy_tree(BUILD_FOLDER, DEPLOY_FOLDER)
print "Copied",len(copied_files),"files"
print "Copied files:"
#print copied_files

# add, commit, push the static blog
os.chdir(DEPLOY_FOLDER)
print "cd", os.getcwd()

run_and_print('git add -A .') 
run_and_print('git commit -m "'+COMMIT_MESSAGE+'"')
run_and_print(push_msg)
