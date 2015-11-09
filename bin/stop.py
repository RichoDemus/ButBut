import sys
import os

def main():
    script_dir = get_script_path()

    pid_path = script_dir + "/PID.txt"

    if not os.path.exists(pid_path):
        print(pid_path + " doesnt exist..")
        return

    file = open(pid_path, "r")

    pid = file.read()

    print("pid is: " + pid)
    print("Stopping ButBut...")
    os.system("kill " + pid)
    os.remove(pid_path)





def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

if __name__ == "__main__":
    main()