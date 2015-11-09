import sys
import os

def main():
    script_dir = get_script_path()

    pid_path = script_dir + "/PID.txt"

    file = open(pid_path, "r")

    pid = file.read()

    print("pid is: " + pid)
    os.system("kill " + pid)
    os.remove(pid_path)





def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

if __name__ == "__main__":
    main()