#we will use the existing functions to convert
import sys, os
import numpy as np
from shutil import copy2

from pyearth.system.define_global_variables import *

from pyearth.toolbox.reader.text_reader_string import text_reader_string



from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces

from pypest.template.shared.pypest_read_configuration_file import pypest_read_pest_configuration_file, pypest_read_model_configuration_file
from pypest.template.shared.xmlchange import xmlchange

from pypest.models.maces.auxiliary.maces_setup_case import maces_setup_case

from pypest.models.maces.multipletimes.step3.maces_convert_minac_parameter_file import maces_convert_minac_parameter_file

from pypest.models.maces.multipletimes.step3.maces_convert_omac_parameter_file import maces_convert_omac_parameter_file



    

#due to the structure of maces, we need to change the path to the calibration folder
def maces_change_file_path(oPest_in, oModel_in):
    iFlag_debug =0
    if iFlag_debug ==1:
        pass
    else:
        pass

    #change the namliest file only

    return



def maces_pypest_convert_parameter_files(oPest_in, oModel_in):
    
    #in order to avoid issue, we will copy the input file into the current folder
    
    
    #maces_change_file_path(oPest_in, oModel_in)

    #next, we need to read the parameter file generated by pest
    #maces_convert_minac_parameter_file(oPest_in, oModel_in)
    maces_convert_omac_parameter_file(oPest_in, oModel_in)
    
    

    return

def run_step3(oPest_in, oModel_in):
    maces_setup_case(oModel_in) #this include the input file
    pypest_convert_parameter_files(oPest_in, oModel_in)
    return

def step3(sFilename_pest_configuration_in, sFilename_model_configuration_in):    
    aParameter_pest  = pypest_read_pest_configuration_file(sFilename_pest_configuration_in)    
    aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration_in
    oPest = pypest(aParameter_pest)
    aParameter_model  = pypest_read_model_configuration_file(sFilename_model_configuration_in)   
    aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration_in
    oMaces = maces(aParameter_model)
    run_step3(oPest, oMaces)
    return

if __name__ == '__main__':
    sFilename_pest_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/pypest.xml'
    sFilename_model_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/model_calibration.xml'    
    step3(sFilename_pest_configuration, sFilename_model_configuration)
    