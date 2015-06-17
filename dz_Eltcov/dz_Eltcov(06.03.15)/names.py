#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import os
import re

def extract_names(filename):
    op = open(filename, 'r')
    str_f = op.read()
    res = re.search('<h3 align="center">.*(\d{4}).*', str_f)
    babynames = [res.group(1)]
    res1 = re.findall('<td>(\d*)</td><td>(\w*)</td><td>(\w*)</td>', str_f)
    for i in res1:
        babynames.extend([i[1]+' - '+i[0]])
        babynames.extend([i[2]+' - '+i[0]])
	babynames.sort()
    return babynames

def main():
    args = sys.argv[1:]
    if not args:
        print 'usage: [--summaryfile] file [file ...]'
        sys.exit(1)
    else:
        summary = False
        if args[0] == '--summaryfile':
            summary = True
            del args[0]
        if not summary:
            list_f = extract_names(args[0])
            for i in list_f:
                print i
        else:
            list_f = extract_names(args[0])
            f = open(list_f[0],'w')
            for i in list_f:
                f.write(i+'\n')
if __name__ == '__main__':
    main()
