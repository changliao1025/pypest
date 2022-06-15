import sys, os
import datetime

from pyearth.system.define_global_variables import *


from retired.pypest_parse_xml_file import pypest_parse_xml_file

pDate = datetime.datetime.today()
sDate_default = "{:04d}".format(pDate.year) + "{:02d}".format(pDate.month) + "{:02d}".format(pDate.day)



def pypest_read_pest_configuration_file(sFilename_configuration_in,\
        sDate_in = None,\
         iCase_index_in=None   ):
         
    config = pypest_parse_xml_file(sFilename_configuration_in)

    sModel = config['sModel']

    if sDate_in is not None:
        sDate = sDate_in
    else:
        sDate = config['sDate']

    if iCase_index_in is not None:
        iCase_index = iCase_index_in
    else:
        iCase_index = int(config['iCase_index'])

    sCase_index = "{:03d}".format(iCase_index)
    #important change here
    config['iCase_index'] = "{:03d}".format(iCase_index)
    sCase = sModel + sDate + sCase_index
    config['sDate'] = sDate
    config['sCase'] = sCase


    return config
    
 
    