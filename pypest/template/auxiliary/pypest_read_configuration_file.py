import sys, os

sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from eslib.system import define_global_variables
from eslib.system.define_global_variables import *

sPath_pypest_python = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest_python'
sys.path.append(sPath_pypest_python)

from pypest.models.maces.inputs.pest_parse_xml_file import pest_parse_xml_file
def pypest_read_configuration_file(sFilename_configuration_in):
    aConfiguration = pest_parse_xml_file(sFilename_configuration_in)
    return aConfiguration
if __name__ == '__main__':
    sFilename_pest_configuration = '/qfs/people/liao313/03configuration/pypest/maces/pest.xml'
    aParameter  = pest_read_configuration_file(sFilename_pest_configuration)
    print(aParameter)    
    