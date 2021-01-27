import sys, os
import datetime
sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyes.system import define_global_variables
from pyes.system.define_global_variables import *

sPath_pypest = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest'
sys.path.append(sPath_pypest)

from pypest.template.shared.pypest_parse_xml_file import pypest_parse_xml_file

pDate = datetime.datetime.today()
sDate_default = "{:04d}".format(pDate.year) + "{:02d}".format(pDate.month) + "{:02d}".format(pDate.day)

def pypest_read_pest_configuration_file(sFilename_configuration_in  ):
         
    config = pypest_parse_xml_file(sFilename_configuration_in)

    


    return config

def pypest_read_model_configuration_file(sFilename_configuration_in,\
        sDate_in = None,\
         iCase_index_in=None   ):
         
    config = pypest_parse_xml_file(sFilename_configuration_in)

    sModel = config['sModel']
    if sDate_in is not None:
        sDate = sDate_in
    else:
        sDate = sDate_default

    if iCase_index_in is not None:
        iCase_index = iCase_index_in
    else:
        iCase_index = 0

    sCase_index = "{:03d}".format(iCase_index)
    #important change here
    config['iCase_index'] = "{:03d}".format(iCase_index)
    sCase = sModel + sDate + sCase_index
    config['sDate'] = sDate
    config['sCase'] = sCase


    return config
if __name__ == '__main__':
    sFilename_pest_configuration = '/qfs/people/liao313/03configuration/pypest/maces/pest.xml'
    aParameter  = pypest_read_configuration_file(sFilename_pest_configuration)
    print(aParameter)    
    