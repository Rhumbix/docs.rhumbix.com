#!/usr/bin/env python

"""Remove all key:value pairs from a json file when the key matches a particular regular experssion."""

from __future__ import print_function
import argparse
import json
import os
import re
import sys

def main(args):
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="A json file to clean.", type=argparse.FileType('r'))
    parser.add_argument('-r', '--regex', help="Any key matching this regular expression will be removed; defualt '^x-amazon.?'", 
                        type=str, default=r'^x-amazon.?', nargs='?')
    parser.add_argument('-o', '--outfile', help="Optional output file, otherwise stdout.",
                        default=sys.stdout, nargs='?', type=argparse.FileType('w'))

    pargs = parser.parse_args(args)
    jdata = json.load(pargs.infile)
    cdata = clean_data(jdata, pargs.regex)
    json.dump(cdata, pargs.outfile, indent=2)

def clean_data(data, regex):
    """Given `data`, clean it."""
    if isinstance(data, dict):
        cdict = dict()
        for k, v in data.iteritems():
            if not re.search(regex, k):
                cdict[k] = clean_data(v, regex)
        return cdict
    elif isinstance(data, list):
        clist = list()
        for item in data:
            clist.append(clean_data(item, regex))
        return clist
    return data

if __name__ == '__main__':
   main(sys.argv[1:])