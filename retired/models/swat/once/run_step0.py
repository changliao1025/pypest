import sys
import os
import numpy as np



from numpy  import array
from pyearth.system.define_global_variables import *


from retired.pypest_read_configuration_file import pypest_read_pest_configuration_file
from retired.pypest_read_configuration_file import  pypest_read_model_configuration_file

from pypest.models.swat.shared.pest import pypest
from pypest.models.swat.once.step0.pypest_prepare_pest_control_file import pypest_prepare_pest_control_file

from pyswat.shared.swat import pyswat
from pyswat.preprocess.auxiliary.swat_prepare_observation_discharge_file import swat_prepare_observation_discharge_file
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




