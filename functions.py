#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
#This is not the main file for the project. It will contain the functions used by the main file
# Author: Andres Zelaya / Opsord

#Description of the program:
#This will be a program that downloads videos from youtube and converts them to a desired format

#The program will follow the following steps:
    #1. Download the video and store on a cache folder
    #2. Convert the video to a desired format and store it on a desired location
    #3. Delete the video from the cache folder
    #4. Repeat the process for all the videos on the list
    #5. Notify the user when the process is done or if there is an error

#Program requirements:
#There will be a text file named "download-list" that will contain the links of the videos to be downloaded
#There will be a text file named "config" that have the following information:
    #1. The final desired format
    #2. The location of the text file with the links
    #3. The location of the cache folder
    #4. The destination of the final file
#The program will create a defa8lt confing and download-list file if they are not found
#The program will be able to read the text file and use the information to download the videos
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
#Importing libraries for downloading the videos
from pytube import YouTube
#Importing libraries for converting the videos
import ffmpeg
#Importing libraries for reading the config file
import json
#Importing libraries for reading the download-list file
import os
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
#Defining the default values for the config file
default_config = {
    "final-format": "mp3",
    "download-list": "download-list.txt",
    "cache-folder": "cache",
    "destination-folder": "downloads"
}

#Defining the default values for the download-list file
default_download_list = [
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley",
]
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
#Defining a function that checks if the config file exists and creates one with default values if it doesn't
def check_config():
    #Checking if the config file exists
    if not os.path.exists("config.json"):
        #Creating the config file
        with open("config.json", "w") as config_file:
            #Writing the default config values to the config file
            json.dump(default_config, config_file, indent=4)

#Defining the function that will read the config file
def read_config():
    #Opening the config file
    with open("config.json", "r") as config_file:
        #Reading the config file
        config = json.load(config_file)
    #Returning the config
    return config

#Defining a function that checks if the download-list file exists and 
# creates one with default values if it doesn't
def check_download_list():
    #Checking if the download-list file exists
    if not os.path.exists("download-list.txt"):
        #Creating the download-list file
        with open("download-list.txt", "w") as download_list_file:
            #Writing the default download-list values to the download-list file
            for link in default_download_list:
                download_list_file.write(link + "\n")

#Defining the function that will read the download-list file and return a list with the links
def read_download_list():
    #Opening the download-list file
    with open("download-list.txt", "r") as download_list_file:
        #Reading the download-list file
        download_list = download_list_file.readlines()
    #Returning the download-list
    return download_list

#Defining the function that will download one video
def download_video(link, cache_folder):
    #Downloading the video
    video = YouTube(link).streams.first().download(cache_folder)
    #Returning the video
    return video

#Defining the function that will convert one video
def convert_video(video, final_format, destination_folder):
    #Converting the video
    ffmpeg.input(video).output(destination_folder + "/" + video.split("/")[-1].split(".")[0] + "." + final_format).run()
    #Returning the video
    return video

#Defining the function that will delete one video
def delete_video(video):
    #Deleting the video
    os.remove(video)
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

