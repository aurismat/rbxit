#! /usr/bin/python3
###############################################################################
# waxmod.py
# Sierra WAX audio file replacer
# by aurismat, 2021
# Based on mj.Jernigan's wax2wav
#
# Usage: py waxmod.py <orgfile.wax> <audiofile.wav>
#
# Requirements: SoX (Sound eXchange) tool from sox.sourceforge.net
#
# You can patch in your own audio into Sierra WAX audio files with this now! Beware that I have only tested this with like a few case scenarios AND with only 1 game, so YMMV.
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

if len(sys.argv) <= 2:
	sys.exit("Usage: vaxmod <orgfile.wax> <filename.wav>")
waxfile = sys.argv[1]
wavfile = sys.argv[2]
print("patching ", wavfile, " into ", waxfile)
#get metadata from OG file
print("Reading original WAX file ", waxfile)
with open(waxfile, 'rb') as f:
    
    headdata = f.read(30)
    fields = struct.unpack("<4sIIHHIIHH2s", headdata)
    waxID,               \
        waxType,         \
        datasize,        \
        wFormatTag,      \
        nChannels,       \
        nSamplesPerSec,  \
        nAvgBytesPerSec, \
        nBlockAlign,     \
        wBitsPerSample,  \
        ckID             = fields
        
    if waxID != WAX_ID:
        print(waxfile, "is not WAX audio.  Skipping.")
        exit()
        
    # Read the rest of the file, then close it to rename it.
    audiodata = f.read()
#get data from new file
print("Reading new audio WAV file ", wavfile)
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
    print("datasize is ", fSize)
    
#write new wax file
print("Overwriting WAX file ", waxfile, " with new audio data")
newlen = (len(data) - 98)
with open(waxfile, "wb") as ff:
    headdata = struct.pack("<4sIIHHIIHH2s",
                            waxID,
                            WAX_PCM,
                            fSize,
                            1,
                            channels,
                            samples,
                            samples*2*channels,
                            2*channels,
                            16,
                            ckID )
    ff.write(headdata)
    ff.write(data)
print("done")
