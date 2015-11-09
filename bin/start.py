import subprocess
import os
import sys
import time


def main():
    script_dir = get_script_path()
    pid_path = script_dir + "/PID.txt"

    if not os.path.exists(pid_path):
        print(pid_path + " already exists..")
        return

    proc = subprocess.Popen(["java", "-jar", script_dir + "/application-1.0-SNAPSHOT.jar", "server", script_dir + "/config.yaml"])
    time.sleep(3)
    pid = proc.pid
    print("The PID is " + str(pid))
    file = open(pid_path, "w")
    file.write(str(pid))





def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

if __name__ == "__main__":
    main()