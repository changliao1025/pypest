import sys, os
import numpy as np
import xml.etree.ElementTree as ET

sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from eslib.system import define_global_variables
from eslib.system.define_global_variables import *

#the pypest library
sPath_pypest_python = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest_python'
sys.path.append(sPath_pypest_python)

from pypest.models.maces.inputs.pest import pypest

from pypest.models.maces.inputs.pest_prepare_maces_control_file import pest_prepare_maces_control_file
from pypest.models.maces.inputs.pest_prepare_maces_instruction_file import pest_prepare_maces_instruction_file

from pypest.models.maces.inputs.template.pest_prepare_maces_parameter_template_files import pest_prepare_maces_parameter_template_files

#from pest_prepare_maces_run_bash_file import pest_prepare_maces_run_bash_file
from pest_read_configuration_file import pest_read_configuration_file


def pest_prepare_all_pest_files(sFilename_pest_configuration):


    aParameter  = pest_read_configuration_file(sFilename_pest_configuration)
    print(aParameter)    
    oPest = pest(aParameter)
    #call each step
    pest_prepare_maces_control_file(oPest)
    pest_prepare_maces_instruction_file()
    #pest_prepare_maces_parameter_template_file()
    #pest_prepare_maces_run_bash_file()


    return

if __name__ == '__main__':
    sFilename_pest_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest_python/pypest/models/maces/config/pypest.xml'
    aParameter  = pest_read_configuration_file(sFilename_pest_configuration)
    print(aParameter)    
    oPest = pypest(aParameter)


    sFilename_model_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest_python/pypest/models/maces/config/model.xml'
    aParameter  = pest_read_configuration_file(sFilename_model_configuration)
    print(aParameter)    
    oMaces = pest(aParameter)
    pest_prepare_maces_control_file(oPest)
