# RBXIT - Really Basic sÍerra Tools
_(the X is x'd out)_

## Fork of the juanitogan's repo with extra tools added;

### You can find the original repo here: https://github.com/juanitogan/rbxit

## Improvements made to the original repository:
* [x] WAX audio replacer in order to mod the audio files;
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
* Copy the .WAX file you want to modify(might take some trial and error, since they have no indication as to which is which(*I might update it later with a list of files*); use `py ./wax2wav.py <file.WAX>` to get a test .wav file) from the extraction folder into the tools directory;
* Once you have your file, get a hold of an audio file you want to patch into the file; You can and *should* export your audio files from Audacity as 'Signed 16-bit PCM';
* Use `py ./waxmod.py <original_wax.WAX> <audio_file_you_want_to_patch_in.WAV>` and it will do it's magic; you can also reuse wax2wav to verify it;
* Put the file you just modified back into the folder you pulled it from, and use `py ./rbx.py <folder_name>`; You should get an unnamed .RBX file inside of the folder.
* Rename the new .RBX file to match the original filename and put it into the game's directory;
* ???
* Profit(?)