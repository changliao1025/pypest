import sys, os
import numpy as np

sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyes.system import define_global_variables
from pyes.system.define_global_variables import *
from pyes.toolbox.reader.text_reader_string import text_reader_string

sPath_pypest_python = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest_python'
sys.path.append(sPath_pypest_python)
from pypest.models.maces.inputs.pest import pest
from pypest.models.maces.outputs.maces_extract_hydrodynamic_output import maces_extract_hydrodynamic_output
from pypest.template.shared.pypest_read_configuration_file import pypest_read_configuration_file

def maces_extract_output_files(oPest_in):
    """
    sFilename_configuration_in
    """
    #stream discharge
    maces_extract_hydrodynamic_output(oPest_in)

def step5(sFilename_pest_configuration_in, sFilename_model_configuration_in):    
    aParameter_pest  = pypest_read_configuration_file(sFilename_pest_configuration)    
    aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration
    oPest = pypest(aParameter_pest)
    aParameter_model  = pypest_read_configuration_file(sFilename_model_configuration)   
    aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration
    oMaces = maces(aParameter_model)
    return
if __name__ == '__main__':
    sFilename_pest_configuration = '/qfs/people/liao313/03configuration/pypest/maces/pest.xml'
    sFilename_model_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/model.xml'    
    step5(sFilename_pest_configuration, sFilename_model_configuration)
    
    
    
   
