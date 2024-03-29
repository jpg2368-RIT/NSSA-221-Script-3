#!/bin/python3

# Joey Guarino
# Mar 2024
# NSSA 221 Script 3

import subprocess as sp

BREAK = "-----------------------------------------------"

# runs a command and returns the result
def run(cmd) -> str:
    proc = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.DEVNULL)
    return str(proc.stdout.read())[2:-3]

# creates a symlink on the user's desktop to a specified file or directory
def create_link() -> None:
    file = input("Enter the name (or the full file path) of the file to link to: ")
    found_file = file if file[0] == "/" else run(f"find / -name {file}")
    if found_file != "" and run(f"ls {found_file}") != "":
        home = run("echo $HOME/Desktop")
        name = input("Enter a name for the symlink: ")
        if run(f"ls {home}/{name}") == "":
            run(f"ln -s {found_file} {home}/{name}")
            print(f"Created a symlink to {found_file} on your desktop named {name}")
        else:
            print(f"Symlink {name} already exists on your desktop...")
    else:
        print(f"File {file} does not exist...")

# deletes an symlink from the user's desktop
def del_link() -> None:
    del_link = input("Enter the name of the link on your desktop that you would like to be deleted: ")
    home = run("echo $HOME")
    if run(f"ls {home}/Desktop/{del_link}") != "":
        run(f"rm $HOME/Desktop/{del_link}")
        print(f"Deleted {del_link}")
    else:
        print(f"Symlink {home}/Desktop/{del_link} does not exist...")

# summarizes the symlinks on the user's desktop
def summary() -> None:
    links = run("find $HOME/Desktop -type l").split("\\n")
    print(f"\nFound {len(links)} symlinks on your desktop\n{BREAK}")
    start = len(run("echo $HOME/Desktop/"))
    for link in links:
        name = link[start:]
        to = run(f"readlink {link}")
        print(f"\t{name}: {to}")

# displays the menu
def menu() -> None:
    print("Shortcuts Menu")
    print(BREAK)
    print("\t{1} Create symbolic link")
    print("\t{2} Delete symbolic link")
    print("\t{3} Summarize links on desktop")
    print("\t{4} Exit")

def main():
    run("clear")
    while True:
        menu()
        choice = input("Enter a choice number: ")
        if choice in {"4", "quit"}:
            break
        if choice == "1":
            create_link()
        elif choice == "2":
            del_link()
        elif choice == "3":
            summary()
        else:
            print(f"Unknowwn choice \"{choice}\", try again...")
        print(f"{BREAK}\n\n")
    print("Exiting program...")
    exit(0)

if __name__ == "__main__":
    main()
