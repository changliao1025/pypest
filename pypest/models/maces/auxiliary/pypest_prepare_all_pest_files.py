import sys, os
import numpy as np
import xml.etree.ElementTree as ET

sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyes.system.define_global_variables import *

#the pypest library
sPath_pypest = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest'
sys.path.append(sPath_pypest)

from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces

from pypest.models.maces.offthegrid.step0 import pypest_prepare_pest_control_file
from pypest.models.maces.offthegrid.step1 import pypest_prepare_pest_template_files
from pypest.models.maces.offthegrid.step2 import pypest_prepare_pest_command_file
from pypest.models.maces.offthegrid.step6 import pypest_prepare_pest_instruction_files

#from pest_prepare_maces_run_bash_file import pest_prepare_maces_run_bash_file
from pypest.template.shared.pypest_read_configuration_file import pypest_read_configuration_file


def pypest_prepare_all_pest_files(oPest_in, oModel_in):


    
    #call each step
    pypest_prepare_pest_control_file(oPest_in, oModel_in)
    pypest_prepare_pest_template_files(oPest_in, oModel_in)
    pypest_prepare_pest_command_file(oPest_in, oModel_in)
    pypest_prepare_pest_instruction_files(oPest_in, oModel_in)

    return


if __name__ == '__main__':
    sFilename_pest_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/pypest.xml'
    sFilename_model_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/model.xml'

    aParameter_pest  = pypest_read_configuration_file(sFilename_pest_configuration)    
    aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration
    oPest = pypest(aParameter_pest)
    aParameter_model  = pypest_read_configuration_file(sFilename_model_configuration)   
    aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration
    oMaces = maces(aParameter_model)
    pypest_prepare_all_pest_files(oPest, oMaces)
