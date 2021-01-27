import sys, os
import numpy as np

sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyes.system.define_global_variables import *

#to be sure we will add the libary here similar to other library
sPath_pypest_python = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest'
sys.path.append(sPath_pypest_python)

from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces

from pypest.template.shared.pypest_read_configuration_file import pypest_read_model_configuration_file

from pypest.models.maces.offthegrid.step6.maces_prepare_minac_instruction_file import maces_prepare_minac_instruction_file

from pypest.models.maces.offthegrid.step6.maces_prepare_omac_instruction_file import maces_prepare_omac_instruction_file

def pypest_prepare_pest_instruction_files(oPest_in, oModel_in):
    """
    prepare pest instruction file
    """
   


    #maces_prepare_minac_instruction_files(oPest_in, oModel_in)
    maces_prepare_omac_instruction_file(oPest_in, oModel_in)
    print('The instruction file is prepared successfully!')

def run_step6(oPest_in, oModel_in):
    pypest_prepare_pest_instruction_files(oPest_in, oModel_in)
    return
def step6(sFilename_pest_configuration_in, sFilename_model_configuration_in):    
    aParameter_pest  = pypest_read_configuration_file(sFilename_pest_configuration)    
    aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration
    oPest = pypest(aParameter_pest)
    aParameter_model  = pypest_read_configuration_file(sFilename_model_configuration)   
    aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration
    oMaces = maces(aParameter_model)

    pypest_prepare_pest_instruction_files(oPest, oMaces)
    return

if __name__ == '__main__':
    sFilename_pest_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/pypest.xml'
    sFilename_model_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/model.xml'    
    step6(sFilename_pest_configuration, sFilename_model_configuration)
    