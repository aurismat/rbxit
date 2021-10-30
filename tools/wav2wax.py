#! /usr/bin/python3
###############################################################################
# wav2wax.py
# WAV to Sierra WAX audio converter
# by aurismat, 2021
# Based on mj.Jernigan's wax2wav
#
# Usage: py wav2wax.py <audiofile.wav> <output_file.wax>
#
# Requirements: SoX (Sound eXchange) tool from sox.sourceforge.net
#
# You can create your own audio in Sierra WAX format now! Beware that I have only tested this with like a few case scenarios AND with only 1 game, so YMMV.
# Audio file should be 16 bit signed PCM for consistency purposes(already provided wax2wav does that for you, or just export Audacity project as 16 bit signed PCM)
# Huge thank you to mj.Jernigan for providing original rbx tools 

# This program is under the terms of GNU GPL license; 
###############################################################################
import sys
#import glob
import os
import struct
import subprocess

WAX_ID    = b"WAX:"
WAX_PCM   = 1
WAX_ADPCM = 4
CK_ID     = b"da"

if len(sys.argv) <= 2:
	sys.exit("Usage: wav2wax <audiofile.wav> <output.wax>")
wavfile = sys.argv[1]
waxfile = sys.argv[2]
#get data from new file
print("Reading audio WAV file ", wavfile)
with open(wavfile, "rb") as ff:
    header = ff.read(44)
    headerfields = struct.unpack("<IIIIIHHIIHH4sI", header)
    chunkID,            \
        chunkSize,      \
        fmt,            \
        Subchunk1ID,    \
        Subchunk1Size,  \
        aFormat,        \
        channels,       \
        samples,        \
        rate,           \
        blockalign,     \
        bits,           \
        dHeader,        \
        fSize           = headerfields;
    data = ff.read()
    
#write new wax file
print("Writing WAX file ", waxfile, " with audio data")
with open(waxfile, "wb") as ff:
    headdata = struct.pack("<4sIIHHIIHH2s",
                            WAX_ID,
                            WAX_PCM,
                            fSize,
                            1,
                            channels,
                            samples,
                            samples*2*channels,
                            2*channels,
                            16,
                            CK_ID )
    ff.write(headdata)
    ff.write(data)
print("done")
