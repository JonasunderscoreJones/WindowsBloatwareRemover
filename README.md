# WindowsBloatwareRemover
A tool that allows for removal of all Preinstalled Apps on Windows that can't be removed by Windows, such as Microsoft Edge

**This tool has been properly tested on Windows 10 and 11**

It is currently being rewritten in Rust at the [rust-dev branch](https://github.com/J-onasJones/WindowsBloatwareRemover/tree/rust-dev).

## How to use
Download the executable of the ![latest releases](https://github.com/J-onasJones/WindowsBloatwareRemover/releases/latest) and run it as administrator.
To do that locate your download folder, right-click the file and click "Run as Administrator"
Windows probably won't run it at first but display a prompt, claiming it had "protected" your pc by blocking the program. Click on "More Info" and then on "Run Anyway".

<a align="center">
<img src="https://github.com/J-onasJones/WindowsBloatwareRemover/blob/main/ReadMeSrc/red1.png" height="250px" width="250px"/><img src="https://github.com/J-onasJones/WindowsBloatwareRemover/blob/main/ReadMeSrc/red2.png" height="250px" width="250px"/>
</a>

Now follow the instructions in the terminal.

**As of version 1.0.0 a proper UI replaces the terminal.** - This will no longer happen in the current version but is being worked on at the [rust-dev branch](https://github.com/J-onasJones/WindowsBloatwareRemover/tree/rust-dev)

*NOTE: Said Version hasn't been released yet.*

### Screenshots
![Terminal Screenshot <v1.0.0](https://github.com/J-onasJones/WindowsBloatwareRemover/blob/main/ReadMeSrc/TerminalScreenshot.png)
![UI Screenshot >=v1.0.0](https://github.com/J-onasJones/WindowsBloatwareRemover/blob/main/ReadMeSrc/UiScreenshot.png)

# Known Issues and Bugs
### Edge won't be removed automatically
The Process to remove the Edge browser doesn't work properly.
There are two steps to permanently remove Microsoft Edge from Windows:
1. The executable needs to be run to uninstall the application itself
2. A registry key needs to be created to tell Windows to not reinstall the browser after a Windows update.

The second step is surprisingly the easy part and can be done with only two commands. But running the uninstaller for the edge browser is way trickier than I originally thought, and here is why:
- The Windows Powershell has issues finding files that are located within the "Program Files (x86)" directory and all of its child directories, meaning all folders and files within that folder which, unfortunately, is where the edge executable is located. There seam to be ways to solve that problem (by using a combination of the alias for the x86 directory but not immediately parsing it into the directory path by defining it as a variable first but my countless tries to achieve that were unsuccessful and right now I am way too frustrated from writing powershell scripts (Ps-script is one of the ugliest shell scripting languages I have ever seen))
- Programmatically running the executable seams to be impossible. When using the default command line to run the command that runs the executable (or running the program in the powershell from the exact location of the uninstall-executable for edge to avoid the x86 issue) windows seams to not run it correctly but when I, as a user, paste the command and run it manually,  it always worked. Either Windows has a built-in function that prevents you from programmatically remove Edge, or I am just a moron.

But just in case, I am working on a solution, and I will (probably) find one. Since I don't use Windows anymore but have switched over Linux a while ago, this is of course not my highest priority so there might not be any updates and bug-fixing in the near future (I also have no time rn).

## Why
Ever used Windows? - I don't think this needs more explanation, especially for 10 and 11.

For everyone else: Microsoft is a master when it comes to slapping bloatware and advertisement onto their operating system, the edge browser being the most prominent one.

I occasionally use Windows virtual machines and despite having a backup that I can easily clone every time I do experiments, etc.., reinstalling a fresh copy of Windows 10 needs to be done from time to time.
