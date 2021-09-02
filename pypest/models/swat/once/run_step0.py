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
from pyswat.preprocess.auxiliary.swat_prepare_observation_discharge_file import swat_prepare_observation_discharge_file
from pyswat.simulation.swat_copy_TxtInOut_files import swat_copy_TxtInOut_files

from pyswat.scenarios.swat_prepare_watershed_parameter_file import swat_prepare_watershed_parameter_file
from pyswat.scenarios.swat_prepare_subbasin_parameter_file import swat_prepare_subbasin_parameter_file
from pyswat.scenarios.swat_prepare_hru_parameter_file import swat_prepare_hru_parameter_file
def run_step0(oPest_in, oSwat_in):

    swat_prepare_observation_discharge_file(oSwat_in)
    #swat_copy_TxtInOut_files(oSwat_in)
    pypest_prepare_pest_control_file(oPest_in, oSwat_in)
    swat_prepare_watershed_parameter_file(oSwat_in)
    swat_prepare_subbasin_parameter_file(oSwat_in)
    swat_prepare_hru_parameter_file(oSwat_in)

    return

def step0(sFilename_pest_configuration_in, sFilename_model_configuration_in):    
    aParameter_pest  = pypest_read_pest_configuration_file(sFilename_pest_configuration_in)    
    aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration_in
    oPest = pypest(aParameter_pest)
    aParameter_model  = pypest_read_model_configuration_file(sFilename_model_configuration_in)   
    aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration_in
    oswat = pyswat(aParameter_model)

    run_step0(oPest, oswat )
    return


