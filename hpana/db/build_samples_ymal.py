#!/usr/bin/env python
"""
Producing a yaml file for samples listed in a txt file.
"""
import re, argparse

##-----------------------------------------------------------------------------------------
## cmd line setup
parser = argparse.ArgumentParser()
parser.add_argument("--ifile", "-i", help="input samples list")
parser.add_argument("--ofile", "-o", help="output ymal file")
args = parser.parse_args()


##-----------------------------------------------------------------------------------------
## consts
PATTERN = re.compile(
    "^(?P<prefix>\S+\.)?"
    "(?P<id>\d+)\."
    "(?P<name>\w+)"
    "(\.\w+\.)"
    "(?P<stream>(AOD|DAOD\_\w+))\."
    "(?P<tag>\S+)$"
)


##-----------------------------------------------------------------------------------------
## main driver
def main():
    with open(args.ifile, "r") as ifile:
        samples  = filter(lambda l: l.startswith("mc"), ifile.readlines())

    snames = set()
    for sample in samples:    
        match = re.match(PATTERN, sample)
        if match:
            name = match.group("name")
            snames.add(name)
        else:
            print sample, "didn't match!!"

    with open(args.ofile, "w") as ofile:
        for sn in sorted(snames):
            ofile.write(sn+"\n")
        
main()

