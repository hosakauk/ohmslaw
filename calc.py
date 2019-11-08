from lib.ohms import ohmslaw
import random
from argparse import ArgumentParser
import sys

def parse_args():
    parser = ArgumentParser(description="Ohms Law Calculator")
    parser.add_argument('-v', '--volts', action='store', dest='volts', type=float)
    parser.add_argument('-r', '--resistance', action='store', dest='resistance', type=float)
    parser.add_argument('-i', '--amps', action='store', dest='amps', type=float)
    parser.add_argument('-p', '--watts', action='store', dest='watts', type=float)
    args = parser.parse_args()
    return args

def getvals():
    args = parse_args()
    ohms = ohmslaw(args.volts,args.resistance,args.amps,args.watts)
    if len(sys.argv) > 3:
        ohms.get_watts()
        ohms.get_amps()
        ohms.get_resistance()
        ohms.get_volts()
        print("%s volts" % ohms.v)
        print("%s resistance" % ohms.r)
        print("%s amps" % ohms.i)
        print("%s watts" % ohms.p)
    else:
        print("Minimum two values required")
        sys.exit(1)
        
getvals()
