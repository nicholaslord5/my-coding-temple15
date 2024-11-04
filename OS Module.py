# 1. Exploring Python's OS Module
# Objective: The goal of this assignment is to deepen your understanding of the OS module in Python.

# Task 1: Directory Inspector:

# Problem Statement: Create a Python script that lists all files and 
# subdirectories in a given directory. Your script should prompt the user for the directory path 
# and then display the contents.

# Code Example:
#    import os

#    def list_directory_contents(path):
#        # List and print all files and subdirectories in the given path
# Expected Outcome: The script should correctly list all files and subdirectories in the 
# specified directory. Handle exceptions for invalid paths or inaccessible directories.

import os

def list_directory_contents(path):
    try:
        if os.path.isdir(path):
            print(f"Contents of '{path}':")
        
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isfile(item_path):
                    print(f"File: {item}")
                elif os.path.isdir(item_path):
                    print(f"Directory: {item}")
        else:
            print("The provided path is not a directory or does not exist.")
    except Exception as e:
        print(f"We've experienced and error: {e}")

directory_path = input("Enter the directory path: ")
list_directory_contents(directory_path)