'''
Created on Feb 7, 2017

@author: chow_vincent
'''

import os                   # Used for file system operations
import shutil               # Used for overwriting directory if it already exists
import json                 # Used for loading JSON data
import urllib.request       # Used for retrieving data from URLs
import requests             # Used for http GET request

access_token = ""
def set_user_access_token(path):
    global access_token
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

    if not found:
        print("No config.txt file found. Please create a file named \"config.txt\" and input your access token.")
        print("Please format your config.txt exactly like...")
        print("access_token=<your access_token here>\n")                    

def create_gallery_dir():
    if not os.path.exists("Photos"):
        print("Creating \"Photos\" folder...")
        os.mkdir("Photos")
    else:
        print("Photos directory already exists.")
        answer = input("Do you want to override your Photos folder, Y or N? ")
        if answer == "Y" or answer == "y" or answer == "yes" or answer == "Yes" or answer == "YES":
            shutil.rmtree("Photos")
            print("Creating \"Photos\" folder...")            
            os.mkdir("Photos")
        elif answer == "N" or answer == "n" or answer == "no" or answer == "No" or answer == "NO":
            exit("Exiting... Please copy over existing files in the Photos folder and try again.")
        else:
            print("Please input Y or N.")
            create_gallery_dir()
        

def main():
    response = requests.get("https://api.instagram.com/v1/users/self/media/recent?access_token=" + str(access_token))
    json_data = json.loads(response.text)
    for index in range(0, len(json_data["data"])):
        pic_url = json_data["data"][index]["images"]["standard_resolution"]["url"]
        print("Creating ig_" + str(index) + ".jpg", "in the Photos directory")
        urllib.request.urlretrieve(pic_url, "Photos/ig_" + str(index) + ".jpg")
            
if __name__ == "__main__":
    print("------------------------------------")    
    print("------------------------------------")
    print("--------Instagram Downloader--------")
    print("------Created by Vincent Chow-------")
    print("------------------------------------")    
    print("------------------------------------\n")
    set_user_access_token(".")
    create_gallery_dir()
    main()
    