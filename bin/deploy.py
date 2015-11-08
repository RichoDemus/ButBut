# richo dont commit this
# scp bin/* pi@raspberrypi:applications/butbut/ && ssh pi@raspberrypi /usr/bin/python /home/pi/applications/butbut/deploy.py cool-hash

import sys
import os
import shutil
from subprocess import call
import time



def main(argv):
    repo = "https://github.com/TSAR-Industries/ButBut.git"
    hash = argv[1]
    print "You want to deploy", hash

    checkout(repo, hash)
    build()
    stop_butbut()
    copy_binaries()
    start_butbut()
    perform_healthcheck_and_rollback_if_failed()


# todo redirect git stdout and errout somewhere else and print our own status messages instead
def checkout(repo, hash):
    source_dir = get_script_path() + "/source"

    print "Deleting old source files in", source_dir
    # if we dont flush here, the printout from git will be printed before
    sys.stdout.flush()
    if os.path.exists(source_dir):
        shutil.rmtree(source_dir)

    call(["git", "clone", repo, source_dir])

    return_code = call(["git", "--git-dir=" + source_dir + "/.git", "--work-tree=" + source_dir, "checkout", hash])
    if return_code != 0:
        print "Checkout failed:", return_code
        quit()

    print "Code checkedout"




def build():
    print "Building"


def stop_butbut():
    print "Stopping ButBut"


def copy_binaries():
    print "Copying new binaries"
    print "Remaking symlink"


def start_butbut():
    print "Startinb ButBut"


def perform_healthcheck_and_rollback_if_failed():
    print "Performing healthcheck"
    print "if failed, rollback"

def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

if __name__ == "__main__":
    main(sys.argv)