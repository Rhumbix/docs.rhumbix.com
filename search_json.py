#!/usr/bin/env python

"""Return the value of a specified key from a provided json file. Follows '.' syntax like 'trunk.branch.limb.leaf'"""

from __future__ import print_function
import argparse
import json
import sys

def main(args):
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="A json file to search.", type=argparse.FileType('r'))
    parser.add_argument('key', type=str, 
        help='Return the value of a key to stdout using "trunk.branch.limb.leaf" syntax. Returns an '\
             'empty string if the key does not exist.')

    pargs = parser.parse_args(args)
    jdata = json.load(pargs.infile)
    try:
        for key in [k for k in pargs.key.split('.') if k]:
            jdata = jdata.get(key)
    except (AttributeError, TypeError, KeyError):
        jdata = ''

    print(jdata)

if __name__ == '__main__':
   main(sys.argv[1:])