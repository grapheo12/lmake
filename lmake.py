#! python3
"""
Live compilation and debugging Script.
=========================================
Usage:
lmake <c-file or make file> [-c <lmake conf file path>]
"""
import argparse
import os
import json

from liveloader import trackFile

parser = argparse.ArgumentParser()
parser.add_argument("file", help="Input file to be compiled")
parser.add_argument("-c", help="Path of the JSON config file")

#Post compile instructions handled through conf file
#TODO: Multiple file tracking

args = parser.parse_args()
fpath = args.file

conf = None
try:
    fp = open(args.c, "r")
    conf = json.load(fp)
except:
    pass
    
trackFile(fpath, conf=conf)