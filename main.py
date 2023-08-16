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
