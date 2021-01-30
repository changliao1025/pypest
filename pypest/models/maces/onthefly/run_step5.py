import sys, os
import numpy as np

sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyes.system.define_global_variables import *


sPath_pypest = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest'
sys.path.append(sPath_pypest)

from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces


from pypest.template.shared.pypest_read_configuration_file import pypest_read_pest_configuration_file, pypest_read_model_configuration_file


from pypest.models.maces.onthefly.step5.maces_extract_omac_output import maces_extract_omac_output

def pypest_extract_model_outputs(oPest_in, oModel_in):
    """
    sFilename_configuration_in
    """
    
    #maces_extract_minac_output(oPest_in, oModel_in)
    maces_extract_omac_output(oPest_in, oModel_in)
    return
def run_step5(oPest_in, oModel_in):
    pypest_extract_model_outputs(oPest_in, oModel_in)
    return
def step5(sFilename_pest_configuration_in, sFilename_model_configuration_in):    
    aParameter_pest  = pypest_read_pest_configuration_file(sFilename_pest_configuration_in)    
    aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration_in
    oPest = pypest(aParameter_pest)
    aParameter_model  = pypest_read_model_configuration_file(sFilename_model_configuration_in)   
    aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration_in
    oMaces = maces(aParameter_model)
    run_step5(oPest, oMaces)
    return
if __name__ == '__main__':
    sFilename_pest_configuration = '/qfs/people/liao313/03configuration/pypest/maces/pest.xml'
    sFilename_model_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/model_sim.xml'    
    step5(sFilename_pest_configuration, sFilename_model_configuration)
    
    
    
   
