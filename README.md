# RBXIT - Really Basic sÍerra Tools
_(the X is x'd out)_

## Fork of the juanitogan's repo with extra tools added;

### You can find the original repo here: https://github.com/juanitogan/rbxit

## Improvements made to the original repository:
* [x] *very* simple WAV to WAX converter;
* [ ] Potentially other modding tools later? 
##### This repository only stores the Python tools used for modifications, as I have no interest in using the other things.
This script and procedure was intended and tested with CyberStorm 1. As I could not do any extensive testing on this, YMMV and use with other games **at your own risk!**

### Requirements for using the tools:
* Python 3;
* SoX Sound Exchanger with it's directory added to PATH;

### As with any guide, ***ALWAYS*** back up your files!

## **Guide on how to modify the audio files:**

* Install the game and get it working in your way of choice(GOG version works for this **but is not recommended**; follow original author's patcher instructions to get the abandonware .iso version working);
* Copy the .rbx files from the game's root directory into your tools directory;
* Using the command `py ./unrbx.py <filename.rbx>`(replacing filename with the file you want to extract, of course), extract the .rbx files into a folder(the script does it for you);
* **Backup** the WAX file you want to replace;
* Get your WAV audio file; Audacity can help you with this, as you can just export your project as a 16-bit signed PCM;
* Use `py ./wav2wax.py <audio_file.wav> <output_file.wax>` and you should have a new WAX file now;
* Use your new file to replace any old file in the extracted file folders, and use `py ./rbx.py <folder_name>`; You should get an unnamed .RBX file inside of the folder.
* Rename the new .RBX file to match the original filename and put it into the game's directory;
* ???
* Profit(?)