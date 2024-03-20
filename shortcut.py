#!/bin/python3.6

# Joey Guarino
# Mar 2024
# NSSA 221 Script 3

import subprocess as sp

BREAK = "-----------------------------------------------"

# runs a command and returns the result
def run(cmd) -> str:
    proc = sp.Popen(cmd, shell=True, stdout=sp.PIPE)
    return str(proc.stdout.read())[2:-3]

def create_link():
    pass

def del_link():
    pass

def summary():
    pass

def menu():
    print("Shortcuts Menu")
    print(BREAK)
    print("\t\{1\} Create symbolic link")
    print("\t\{2\} Delete symbolic link")
    print("\t\{3\} Summarize links on desktop")
    print("\t\{4\} Exit")

def main():
    run("clear")
    while True:
        menu()
        choice = input("Enter a choice number: ")
        if choice == "4":
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
