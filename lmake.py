#! python3
"""
Live compilation and debugging Script.
=========================================
Usage:
lmake <c-file or make file> [-c <lmake conf file path>] [-i <input file>]
"""
import argparse
import os
import json

from liveloader import trackFile

parser = argparse.ArgumentParser()
parser.add_argument("file", help="Input file to be compiled")
parser.add_argument("-c", help="Path of the JSON config file")
parser.add_argument("-i", help="Input file")
#Post compile instructions handled through conf file
#TODO: Multiple file tracking

args = parser.parse_args()
fpath = args.file

conf = None
try:
    fp = open(args.c, "r")
    conf = json.load(fp)
    fp.close()
except:
    name, extension = os.path.splitext(fpath)
    try:
        fp = open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
        "config/{}.json".format(extension[1:])), "r")

        conf = json.load(fp)
        fp.close()
    except:
        pass
        
try:
    fi = open(args.i, "r")
    trackFile(fpath, conf=comp, istream=fi)
except:
    trackFile(fpath, conf=conf)