import sys
import os
import numpy as np
import datetime
import calendar


from numpy  import array
from pyearth.system.define_global_variables import *


from pyearth.toolbox.reader.text_reader_string import text_reader_string
from pypest.template.shared.pypest_read_configuration_file import pypest_read_pest_configuration_file
from pypest.template.shared.pypest_read_configuration_file import  pypest_read_model_configuration_file

from pypest.models.swat.shared.pest import pypest
from pyswat.shared.swat import pyswat

from pypest.models.swat.once.step0.pypest_prepare_pest_control_file import pypest_prepare_pest_control_file
from pypest.models.swat.auxiliary.swat_prepare_observation_discharge_file import swat_prepare_observation_discharge_file
from pyswat.simulation.swat_copy_TxtInOut_files import swat_copy_TxtInOut_files
def run_step0(oPest_in, oModel_in):

    swat_prepare_observation_discharge_file(oModel_in)
    swat_copy_TxtInOut_files(oModel_in)
    pypest_prepare_pest_control_file(oPest_in, oModel_in)
    return

def step0(sFilename_pest_configuration_in, sFilename_model_configuration_in):    
    aParameter_pest  = pypest_read_pest_configuration_file(sFilename_pest_configuration)    
    aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration
    oPest = pypest(aParameter_pest)
    aParameter_model  = pypest_read_model_configuration_file(sFilename_model_configuration)   
    aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration
    oswat = pyswat(aParameter_model)

    run_step0(oPest, oswat )
    return

if __name__ == '__main__':

    

    sFilename_pest_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/swat/config/pypest.xml'
    sFilename_model_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/swat/config/swat_calibration.xml'    
    step0(sFilename_pest_configuration, sFilename_model_configuration)
