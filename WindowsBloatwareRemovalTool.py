VERSION = "0.1.2"

import os
import ctypes
from sys import exit as sysexit
import sys
import acceptdestruction, adminprompt, done, mainwindow, process
from PyQt5 import QtGui

def isAdmin():
	try:
		if ctypes.windll.shell32.IsUserAnAdmin():
			return True
		else:
			return False
	except:
		return False

modeOptions = ["1", "2", "3", "4", "5", "6", "q"]
modeOptionsDisplay = str(modeOptions).replace("'", "").replace(",", "/").replace(" ", "")
requireAdmin = ["1", "2", "3", "4", "5", "6"]
requireAdminDisplay = str(requireAdmin).replace("'", "").replace(",", "/").replace(" ", "")
apps = ["3D Builder", "Alarms", "Calculator", "Communications", "Camera", "Cortana", "Get Office", "Skype", "Get Started", "Groove Music", "Maps", "News", "One Note", "People", "Solitaire Collection", "Finance", "Video & TV", "Photos", "Microsoft Store", "Sports", "Voice Recorder", "Weather", "Xbox", "Xbox Gaming Overlay", "Get Help", "Your Phone", "Cortana", "Edge"]
appsIDs = ["3d", "windowsalarms", "windowscalculator", "windowscommunicationsapps", "windowscamera", "officehub", "skypeapp", "getstarted", "zunemusic", "windowsmaps", "bingnews", "onenote", "people", "solitairecollection", "bingfinance", "zunevideo", "zunemusic", "photos", "windowsstore", "bingsports", "soundrecorder", "bingweather", "xboxapp", "Microsoft.XboxGamingOverlay", "Microsoft.GetHelp", "YourPhone", "Microsoft.549981C3F5F10", None]
removeApp = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
appsBing = ["Finance", "News", "Sports", "Weather"]
appsBingIDs = ["bingfinance", "bingnews", "bingsports", "bingweather"]
appsXbox = ["Xbox", "Xbox Gaming Overlay"]
appsXboxIDs = ["xboxapp", "Microsoft.XboxGamingOverlay"]
appsUsual = ["3D Builder", "Alarms", "Communications", "Camera", "Cortana", "Get Office", "Skype", "Get Started", "Groove Music", "Maps", "News", "One Note", "People", "Solitaire Collection", "Finance", "Sports", "Voice Recorder", "Weather", "Xbox", "Get Help", "Your Phone", "Cortana", "Edge"]
appsUsualIDs = ["3d", "windowsalarms", "windowscommunicationsapps", "windowscamera", "officehub", "skypeapp", "getstarted", "zunemusic", "windowsmaps", "bingnews", "onenote", "people", "solitairecollection", "bingfinance", "bingsports", "soundrecorder", "bingweather", "xboxapp", "Microsoft.GetHelp", "YourPhone", "Microsoft.549981C3F5F10", None]


# if not isAdmin():
# 	adminprompt.show()

mainwindow.show()



mode = input("Select " + modeOptionsDisplay + ":")

def execPowershell(cmd):
	cmd = "powershell -command \"" + cmd + "\""
	os.system(cmd)

# define Edge removal as separate function as it requires special Steps
def rmEdge():
	# Required Steps to permanently remove edge:
	# 	- Run the edge setup executable with flags to remove it from the system
	# 	- create a ew Registry Key including an entry for windows to not reinstall edge after a new update (because beleive it or not, windows has it as a built-in feature to reinstall Edge after updates if it detects that the user has removed it)
	edgeFolders = [ f.path for f in os.scandir("C:/Program Files (x86)/Microsoft/Edge/Application/") if f.is_dir() ]
	for i in range(len(edgeFolders)):
			if not "." in edgeFolders[i - 1]:
				edgeFolders.pop(i - 1)
	if len(edgeFolders) == 1:
		command = edgeFolders[0] + "/Installer/setup --uninstall --force-uninstall --system-level"
	else:
		print("\n USER INPUT REQUIRED\n")


		for i in range(len(edgeFolders)):
			print("\t" + str(i) + ") " + edgeFolders[i - 1].replace("C:/Program Files (x86)/Microsoft/Edge/Application/", ""))
		dirIndex = input("Type the number (eg. '1)') of the folder that is similar to '101.0.1210.53': ")
		while not dirIndex <= str(len(edgeFolders) - 1):
			print("WRONG NUMBER")
			dirIndex = input("Type the number (eg. '1)') of the folder that is similar to '101.0.1210.53': ")
		#execPowershell("ls 'C:\Program Files (x86)\Microsoft\Edge\Application'")
		command = edgeFolders[int(dirIndex) - 1] + "/Installer/setup --uninstall --force-uninstall --system-level"
	print(command)
	execPowershell(command)
	# prevent Edge from reinstalling after updates by creating a registry key

	# create new registry key
	execPowershell("New-Item -Path 'HKLM:\SOFTWARE\Microsoft' -Name EdgeUpdate")
	# create entry within the newly created key
	execPowershell("New-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\EdgeUpdate' -Name  'DoNotUpdateToEdgeWithChromium' -Value '1' -PropertyType 'DWORD' -Force")

def rmApp(id, name):
	if name == "Edge":
		# remove edge
		rmEdge()
	else:
		command = "Get-AppxPackage *" + id + "* | Remove-AppxPackage"
		execPowershell(command)
	print("Removed " + name)

def rmList(list, listNames, removeApp):
	for i in range(len(list)):
		if removeApp[i-1]:
			rmApp(list[i-1], listNames[i-1])

# if no valid mode selected
while mode not in modeOptions:
	print("'" + mode + "' IS INVALID.")
	mode = input("PLEASE SELECT ONE OF THE FOLLOWING: " + modeOptionsDisplay + ":")

# run the selected mode
if mode == "q":
	print("Quitting.")
	sysexit()
else:
	agreeToDistruction = None
	print("\nBy using this program, any possible damage to your Windows Installation is Your Responsability and NOT this scripts Author's.")
	while agreeToDistruction != 'y' and agreeToDistruction != 'n':
		agreeToDistruction = input("\nBy typing 'y' (lowercase y) for yes You agree to the above point. By typing anything else, the program will abort. [y/n]: ")
	
	if agreeToDistruction == "n":
		print("Aborting due to decline...")
		sysexit()
		sysexit()
	else:
		if mode == "1":
			print("Removing all Unremovable Apps")
			rmList(appsIDs, apps, removeApp)
		elif mode == "2":
			print("Removing all Bing related Apps")
			rmList(appsBingIDs, appsBing, removeApp)
		elif mode == "3":
			print("Removing all XboX related Apps")
			rmList(appsXboxIDs, appsXbox, removeApp)
		elif mode == "4":
			print("Removing all Apps that are usually removed")
			rmList(appsUsualIDs, appsUsual, removeApp)
		elif mode == "5":
			print("Removing the Microsoft Edge Browser")
			rmEdge()
		elif mode == "6":
			print("Removing a custom Selection of Apps")
			print("Answer the following by typing a lowercase 'n' for NO or a lowercase 'y' for YES and hit enter\n")
			for i in range(len(apps)):
				yesno = input("\tRemove " + apps[i-1] + "?")
				while yesno != "y" and yesno != "n":
					print("\nPlease enter 'y' for yes and 'n' for no.")
					yesno = input("\tRemove " + apps[i-1] + "?")
				if yesno == "n":
					removeApp[i-1] = False
			print("Starting to remove apps...")
			rmList(appsIDs, apps, removeApp)
		else:
			print("Whoops. Something went wrong. This case should be programatically impossible but I might just have done some fucky wucky mistake that allows this case to be legal. We could also just blame it all on python. In reality I am just writing a short error message that has suddenly become very long and I just keep writing and no one will ever see this anyway...")
			sysexit()
print("All done!")