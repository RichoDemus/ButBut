# Continuous Deployment script for ButBut
# This script will:
# 1. checkout the code
# 2. build
# 3. put the files needed to run in a directory named after the commit hash
# 4. stop the old ButBut instance
# 5. update a symlink called "latest" to point to the new directory
# 6. start ButBut
#
# This script is intended to be run from a CI server like this: ssh user@host path/deploy.sh commit-hash
#
# todo: perform a healthcheck of the new instance and rollback if it failed

# richo dont commit this
# scp bin/* pi@raspberrypi:applications/butbut/ && ssh pi@raspberrypi /usr/bin/python /home/pi/applications/butbut/deploy.py cool-hash

import sys
import os
import shutil
import subprocess
import time
import distutils.core


def main(argv):
    #repo_url = "https://github.com/TSAR-Industries/ButBut.git"
    repo_url = "https://github.com/RichoDemus/ButBut.git"
    source_dir = get_script_path() + "/source"
    jar_path = source_dir + "/application/target/butbut.jar" # change to this before checkin, if you can read this, reject this PR :p
    #jar_path = source_dir + "/application/target/application-1.0-SNAPSHOT.jar"
    script_path = source_dir + "/bin"
    hash = argv[1]
    install_dir = get_script_path() + "/" + hash
    config_file_path = source_dir + "/config.yaml"
    latest_deliverables_dir = get_script_path() + "/latest"

    print("You want to deploy", hash)

    remove_old_sources(source_dir)
    checkout(source_dir, repo_url, hash)
    build(source_dir)
    check_new_binary(jar_path)
    copy_deliverables(jar_path, script_path, config_file_path, install_dir)
    stop_butbut(latest_deliverables_dir)
    create_symlink(install_dir, latest_deliverables_dir)
    start_butbut(latest_deliverables_dir)
    perform_healthcheck_and_rollback_if_failed()


def remove_old_sources(source_dir):
    print("Deleting old source files in", source_dir)
    # if we dont flush here, the printout from git will be printed before
    sys.stdout.flush()
    if os.path.exists(source_dir):
        shutil.rmtree(source_dir)


# todo redirect git stdout and errout somewhere else and print our own status messages instead
def checkout(source_dir, repo, hash):
    subprocess.call(["git", "clone", repo, source_dir])

    return_code = subprocess.call(["git", "--git-dir=" + source_dir + "/.git", "--work-tree=" + source_dir, "checkout", hash])
    if return_code != 0:
        print("Checkout failed:", return_code)
        quit()

    print("Code checkedout")


def build(source_dir):
    pom_dir = source_dir + "/pom.xml"
    print("Building", pom_dir)
    subprocess.call(["mvn", "-f", pom_dir, "clean", "install"])


def check_new_binary(jar_path):
    if not os.path.exists(jar_path):
        print("Cant find jar-file:",jar_path)
        quit()
    print("jar-file found")


def stop_butbut(latest_deliverables_dir):
    os.chmod(latest_deliverables_dir + "/butbut.sh", 0o700)
    subprocess.call([latest_deliverables_dir + "/butbut.sh", "stop"])

def copy_deliverables(jar_path, script_path, config_file_path, install_dir):
    print("Copying new binaries to " + install_dir)
    if not os.path.exists(install_dir):
        os.mkdir(install_dir)

    shutil.copy(jar_path, install_dir)
    shutil.copy(config_file_path, install_dir)

    print("copying contents of " + script_path + " to " + install_dir)
    distutils.dir_util.copy_tree(script_path, install_dir)
    os.chmod(install_dir + "/butbut.sh", 0o700)


def create_symlink(install_dir, latest_deliverables_dir):
    print("Remaking symlink")
    if os.path.exists(latest_deliverables_dir):
        os.unlink(latest_deliverables_dir)
    os.symlink(install_dir, latest_deliverables_dir)


def start_butbut(latest_deliverables_dir):
    subprocess.call([latest_deliverables_dir + "/butbut.sh", "start"])


def perform_healthcheck_and_rollback_if_failed():
    print("Should maybe check if ButBut is running ok?")


def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

if __name__ == "__main__":
    main(sys.argv)