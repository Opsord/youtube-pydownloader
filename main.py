#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
#This is the main file for the project. It will be used to run the program
#It will also be used to call the other files and functions
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
#Importing libraries for accessing the config file
import json
#Importing libraries for accessing the download-list file
import os
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
#Importing the functions from the functions file
from functions import check_config, read_config, check_download_list, read_download_list
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
#Here is where the program starts


#Getting the config values

#Checking if the config file exists and creating one with default values if it doesn't
check_config()
#Reading the config file
config = read_config()
#Checking if the download-list file exists and creating one with default values if it doesn't
check_download_list()
#Reading the download-list file
download_list = read_download_list()

#Download the first video on the list
video = YouTube(download_list[0])
#Getting the title of the video
video_title = video.title
#Getting the video stream (lowest resolution since the final formar is mp3)
video_stream = video.streams.get_lowest_resolution()
#Downloading the video to the cache folder
video_stream.download(config["cache-folder"])
#Converting the video to mp3


# #Downloading and converting the videos
# for videoLink in download_list:
#     #Downloading the video
#     video = YouTube(videoLink)
#     #Getting the title of the video
#     videoTitle = video.title
#     #Getting the video stream (lowest resolution since the final formar is mp3)
#     videoStream = video.streams.get_lowest_resolution()
#     #Downloading the video
#     videoStream.download()
#     #Converting the video to mp3
#     ffmpeg.input(videoTitle).output(videoTitle + ".mp3").run()
#     #Deleting the video from the cache folder
#     os.remove(videoTitle)
#     #Moving the video to the destination folder
#     os.rename(videoTitle + ".mp3", config["destination-folder"] + "/" + videoTitle + ".mp3")



#Displaying config values to the user
print("The config values are:")
print(config)


#Displaying a message to the user when the program is done
print("The program has finished downloading and converting the videos")

#Deleting the contents of the cache folder
for file in os.listdir(config["cache-folder"]):
    os.remove(config["cache-folder"] + "/" + file)

#Displaying a message to the user when the program is done
print("The program has finished deleting the videos from the cache folder")