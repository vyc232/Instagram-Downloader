'''
Created on Feb 7, 2017

@author: chow_vincent
'''

import os       # Used for file system operations
import shutil   # Used for overwriting directory if it already exists

access_token = ""
def set_user_access_token(path):
    found = False
    for entry in os.scandir(path):
        if not entry.name.startswith(".") and entry.is_file() and entry.name == "config.txt":
            found = True
            with open(entry.name, "r") as config_file:
                for line in config_file:
                    if "access_token" in line:
                        access_token = line.split("=")[1]
                        if access_token == "" or access_token == "\n":
                            print("Access Token not found. Please fix config.txt")
                            print("Please format your config.txt exactly like...")
                            print("access_token=<your access_token here>\n") 
                            exit("Exiting due to issue finding access token")
                        else:
                            print("Access Token found...")
    if not found:
        print("No config.txt file found. Please create a file named \"config.txt\" and input your access token.")
        print("Please format your config.txt exactly like...")
        print("access_token=<your access_token here>\n")                    

def create_gallery_dir():
    if not os.path.exists("Photos"):
        print("Creating \"Photos\" folder...")
        os.mkdir("Photos")
    else:
        answer = input("Do you want to override your Photos folder, Y or N? ")
        if answer == "Y" or answer == "y" or answer == "yes" or answer == "Yes" or answer == "YES":
            shutil.rmtree("Photos")
            print("Creating \"Photos\" folder...")            
            os.mkdir("Photos")
        elif answer == "N" or answer == "n" or answer == "no" or answer == "No" or answer == "NO":
            exit("Exiting... Please copy over existing files in the Photos folder and try again")
        else:
            print("Please input Y or N.")
            create_gallery_dir()
        
        
        
        
            
                
                    


if __name__ == "__main__":
    print("------------------------------------")    
    print("------------------------------------")
    print("--------Instagram Downloader--------")
    print("------Created by Vincent Chow-------")
    print("------------------------------------")    
    print("------------------------------------\n")
    set_user_access_token(".")
    create_gallery_dir()
    