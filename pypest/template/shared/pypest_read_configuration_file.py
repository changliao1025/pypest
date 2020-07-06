import sys, os

sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyes.system import define_global_variables
from pyes.system.define_global_variables import *

sPath_pypest = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest'
sys.path.append(sPath_pypest)

from pypest.template.shared.pypest_parse_xml_file import pypest_parse_xml_file

def pypest_read_configuration_file(sFilename_configuration_in):
    aConfiguration = pest_parse_xml_file(sFilename_configuration_in)
    return aConfiguration
if __name__ == '__main__':
    sFilename_pest_configuration = '/qfs/people/liao313/03configuration/pypest/maces/pest.xml'
    aParameter  = pypest_read_configuration_file(sFilename_pest_configuration)
    print(aParameter)    
    