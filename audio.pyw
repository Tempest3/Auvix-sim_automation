#!C:/Python33/pythonw.exe
from subprocess import call, STARTUPINFO

def AudioFunc(arg1):
	
	#set window properties...
	info = STARTUPINFO()
	info.dwFlags = 1
	info.wShowWindow = 0
	
	#audio...
	options = {0 : "military.mp3", 1: "ww2.mp3", 2: "caribbean.mp3"}	
	audio_clip = options[arg1]	
	audio_path = 'C:\\Users\\Auvix Demo\\Documents\\music\\'
	vlc_path = 'C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe'

	
	
	call([vlc_path , audio_path + audio_clip, "-I", "-R"], startupinfo=info)