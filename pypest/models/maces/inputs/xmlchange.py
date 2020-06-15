#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:21:26 2020

Modify the specified model parameter in the specified file 

"""

import sys
import numpy as np
import xml.etree.ElementTree as ET
from optparse import OptionParser

# use the OptionParser to parse the command line options

def xmlchange():
    parser = OptionParser()
    parser.add_option("-f", "--file", type="string", dest="filename")
    parser.add_option("-g", "--group", type="string", dest="group", default=None)
    parser.add_option("-p", "--parameter", type="string", dest="parameter")
    parser.add_option("-v", "--value", type="string", dest="value", default=None)
    parser.add_option("-s", "--values", type="string", nargs=10, 
                      dest="values", default=None)

    (options, args) = parser.parse_args()

    try:
        # extract arguments and check
        filename = options.filename
        group = options.group
        parameter = options.parameter
        value = options.value
        values = options.values
        assert np.logical_xor(options.value==None,options.values==None), \
            "both -v and -s are present or neither of them are present."

        # for hydrodynamics parameters
        isfind = False
        if group==None:
            # set the parameter
            if values==None:
                # find the node and modify its value
                tree = ET.parse(filename)
                root = tree.getroot()
                findstr = "./entry"
                for entry in root.findall(findstr):
                    if entry.get('id')==parameter:
                        isfind = True
                        entry.set('value', value)
            else:
                # find the node and modify its values
                tree = ET.parse(filename)
                root = tree.getroot()
                findstr = "./entry"
                for entry in root.findall(findstr):
                    if entry.get('id')==parameter:
                        isfind = True
                        for value in entry.findall('values/value'):
                            pft = int(value.get('pft'))
                            value.text = values[pft]
        else:
            # set the parameter
            if values==None:
                # find the node and modify its value
                tree = ET.parse(filename)
                root = tree.getroot()
                findstr = "./group/[@id='" + group + "']/entry"
                for entry in root.findall(findstr):
                    if entry.get('id')==parameter:
                        isfind = True
                        entry.set('value', value)
            else:
                # find the node and modify its values
                tree = ET.parse(filename)
                root = tree.getroot()
                findstr = "./group/[@id='" + group + "']/entry"
                for entry in root.findall(findstr):
                    if entry.get('id')==parameter:
                        isfind = True
                        for value in entry.findall('values/value'):
                            pft = int(value.get('pft'))
                            value.text = values[pft]
        assert isfind, "parameter " + parameter + " is not found in the xml file"
        # write to xml file
        tree.write(filename)
    except AssertionError as errstr:
        # print error message and exit the program
        print("xmlchange fails due to that", errstr)
        sys.exit()
if __name__ == '__main__':
    xmlchange()