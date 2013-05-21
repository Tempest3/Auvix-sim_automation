#!C:/Python33/pythonw.exe

#Auvix Automation Software
#Written by Konrad Wiley on 5/18/2013
#For Python 3.3.2

#import os and subprocess modules
from os import system
import sys
from subprocess import call, STARTUPINFO
from multiprocessing import Process
import audio


if __name__ == '__main__':
	
	#set window properties...
	info = STARTUPINFO()
	info.dwFlags = 1
	info.wShowWindow = 0

	#Video ==================================
	#file paths...
	video_path = 'C:\\Users\\Auvix Demo\\Documents\\test_vid.mov'
	vlc_path = 'C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe'

	#play the video clip... exit vlc when done
	call([vlc_path, video_path, "--plugin-path=" + vlc_path,"--play-and-exit","--fullscreen"], startupinfo=info)
	#========================================

	#Prepar3D ===============================
		
	if len(sys.argv) > 1:
		p = Process(target=audio.AudioFunc, args=(int(sys.argv[1]),))
		p.start()

	#launch Prepar3D
	prepar3d_path = "C:\\Program Files (x86)\\Lockheed Martin\\Prepar3D\\Prepar3D.exe"
	call([prepar3d_path])

	if len(sys.argv) > 1:
		system('taskkill /f /im vlc.exe')

	system("shutdown /p")