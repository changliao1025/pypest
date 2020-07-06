import sys, os
import numpy as np
import xml.etree.ElementTree as ET

sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyes.system import define_global_variables
from pyes.system.define_global_variables import *

#the pypest library
sPath_pypest = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest'
sys.path.append(sPath_pypest)

from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces

from pypest.models.maces.offthegrid.step0.pypest_prepare_pest_control_file import pypest_prepare_pest_control_file
from pypest.models.maces.offthegrid.step1.pypest_prepare_pest_template_files import pypest_prepare_pest_template_files
from pypest.models.maces.offthegrid.step2.pypest_prepare_pest_command_file import pypest_prepare_pest_command_file
from pypest.models.maces.offthegrid.step6.pypest_prepare_pest_instruction_files import pypest_prepare_pest_instruction_files

#from pest_prepare_maces_run_bash_file import pest_prepare_maces_run_bash_file
from pypest.template.shared.pypest_read_configuration_file import pypest_read_configuration_file


def pypest_prepare_all_pest_files(oPest, oModel):


    #aParameter  = pest_read_configuration_file(sFilename_pest_configuration)
    #print(aParameter)    
    #oPest = pest(aParameter)
    #call each step
    pypest_prepare_pest_control_file(oPest, oModel)
    pypest_prepare_pest_template_files(oPest, oModel)
    pypest_prepare_pest_command_file(oPest, oModel)
    pypest_prepare_pest_instruction_files(oPest, oModel)

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
    pypest_prepare_all_pest_files(oPest)
